import streamlit as st
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

st.title("Azure AI Foundry Chat Assistant")

# Initialize Azure OpenAI client
@st.cache_resource
def get_azure_client():
    """Initialize AzureOpenAI client with proper error handling."""
    try:
        # Get configuration from environment variables or Streamlit secrets
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        api_version = "2024-12-01-preview"
        
        if not endpoint:
            st.error("AZURE_OPENAI_ENDPOINT not found in environment variables or Streamlit secrets.")
            st.stop()
            
        if not api_key:
            st.error("AZURE_OPENAI_API_KEY not found in environment variables or Streamlit secrets.")
            st.stop()
        
        # Create AzureOpenAI client
        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=api_key,
        )
        
        return client
    
    except Exception as e:
        st.error(f"Failed to initialize Azure OpenAI client: {str(e)}")
        st.error("Please check your Azure OpenAI configuration.")
        st.stop()

# Initialize client
chat_client = get_azure_client()

# Available model deployments (update these to match your deployed models)
AVAILABLE_MODELS = [
    "gpt-5-mini",
    "gpt-4o",
    "gpt-4o-mini",
]

# Set a default model
if "azure_model" not in st.session_state:
    st.session_state["azure_model"] = "gpt-5-mini"

# Sidebar for model selection and settings
with st.sidebar:
    st.title("🤖 Azure AI Settings")
    
    # Model selection
    selected_model = st.selectbox(
        "Choose AI Model:",
        AVAILABLE_MODELS,
        index=AVAILABLE_MODELS.index(st.session_state["azure_model"]) if st.session_state["azure_model"] in AVAILABLE_MODELS else 0,
        help="Select the Azure OpenAI deployment to use for chat"
    )
    
    # Update session state if model changed
    if selected_model != st.session_state["azure_model"]:
        st.session_state["azure_model"] = selected_model
        st.rerun()
    
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption(f"Current Model: **{st.session_state['azure_model']}**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        try:
            # Show thinking indicator
            message_placeholder = st.empty()
            full_response = ""
            
            # Prepare messages for the API call
            messages_for_api = [
                {"role": "system", "content": "You are a helpful AI assistant powered by Azure AI Foundry. Provide clear, accurate, and helpful responses."}
            ] + st.session_state.messages
            
            # Try streaming first, fallback to non-streaming if issues occur
            try:
                # Call Azure OpenAI chat completion with streaming
                response = chat_client.chat.completions.create(
                    model=st.session_state["azure_model"],
                    messages=messages_for_api,
                    stream=True
                )
                
                # Stream the response
                for chunk in response:
                    if chunk.choices and len(chunk.choices) > 0:
                        if hasattr(chunk.choices[0], 'delta') and chunk.choices[0].delta and chunk.choices[0].delta.content:
                            full_response += chunk.choices[0].delta.content
                            message_placeholder.markdown(full_response + "▌")
                
                # Final response without cursor
                message_placeholder.markdown(full_response)
                
            except Exception:
                # Fallback to non-streaming mode
                st.warning("Streaming failed, using non-streaming mode...")
                response = chat_client.chat.completions.create(
                    model=st.session_state["azure_model"],
                    messages=messages_for_api,
                    stream=False
                )
                
                full_response = response.choices[0].message.content
                message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Error generating response: {str(e)}")
            st.error("Please check your Azure OpenAI setup and model deployment.")
            full_response = f"Sorry, I encountered an error: {str(e)}"
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
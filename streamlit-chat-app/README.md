# Azure OpenAI Streamlit Chat App

A modern chat application powered by Azure OpenAI models with a clean Streamlit interface.

## Features

- 🤖 **Multiple AI Models**: Choose from various Azure OpenAI deployments (gpt-5-mini, gpt-4o, etc.)
- 💬 **Real-time Streaming**: See responses as they're generated
- 🔒 **Secure Configuration**: Uses API keys for authentication
- 📱 **Responsive UI**: Clean, modern interface with sidebar controls
- 🗑️ **Chat Management**: Clear chat history with one click

## Prerequisites

1. **Azure OpenAI Service**: You need an Azure OpenAI resource with deployed models
2. **API Key**: Your Azure OpenAI API key
3. **Environment Variables**: Set `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY`

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements-streamlit.txt
```

### 2. Set Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Then edit `.env` and set your Azure OpenAI configuration:

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
```

Or add them to your Streamlit secrets in `.streamlit/secrets.toml`:

```toml
AZURE_OPENAI_ENDPOINT = "https://your-resource.cognitiveservices.azure.com/"
AZURE_OPENAI_API_KEY = "your-api-key-here"
```

### 3. Run the Application

```bash
streamlit run src/chat.py
```

## Available Models

The application supports the following Azure OpenAI model deployments (ensure they're deployed in your resource):

- **gpt-5-mini**: Lightweight version for cost-sensitive applications
- **gpt-4o**: Multimodal model handling text and image inputs
- **gpt-4o-mini**: Affordable, efficient AI for diverse tasks

Note: Update the `AVAILABLE_MODELS` list in `chat.py` to match your actual model deployments.

## Configuration

### Temperature
- **Range**: 0.0 - 2.0
- **Default**: 0.7
- **Lower values**: More focused and deterministic responses
- **Higher values**: More creative and varied responses

### Max Tokens
- **Range**: 50 - 4000
- **Default**: 1000
- **Controls**: Maximum length of generated responses

## Security Features

- API keys stored securely in environment variables or Streamlit secrets
- No credentials hardcoded in source code
- Environment-based configuration for different deployments

## Troubleshooting

### Authentication Issues
- Verify your API key is correct and active
- Check that the endpoint URL is properly formatted
- Ensure you have proper permissions on the Azure OpenAI resource

### Model Deployment Issues
- Verify models are deployed in your Azure OpenAI resource
- Check deployment names match exactly with the names in `AVAILABLE_MODELS`
- Ensure sufficient quota for the selected models

### Connection Issues
- Verify network connectivity to Azure
- Check firewall settings if running behind corporate network
- Ensure the endpoint URL is correct and accessible

## File Structure

```
streamlit-chat-app/
├── src/
│   └── chat.py              # Main Streamlit application
├── requirements-streamlit.txt    # Python dependencies
└── README.md               # This documentation
```

## Development

To modify or extend the application:

1. **Add New Models**: Update the `AVAILABLE_MODELS` list in `chat.py`
2. **Customize UI**: Modify the Streamlit components in the main application
3. **Add Features**: Extend the sidebar or chat functionality as needed
4. **Error Handling**: Enhance error messages and recovery mechanisms

## Best Practices

- **Model Selection**: Start with smaller models (gpt-5-mini, phi-4-mini) for development
- **Cost Management**: Monitor usage and set appropriate limits
- **Performance**: Use streaming for better user experience
- **Security**: Never hardcode credentials or endpoints in source code

## Support

For issues related to:
- **Azure AI Foundry**: Check Azure documentation and service health
- **Streamlit**: Refer to Streamlit documentation
- **Authentication**: Verify Azure CLI and credential setup
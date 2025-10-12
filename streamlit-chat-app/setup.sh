#!/bin/bash
# Setup script for Azure OpenAI Streamlit Chat App

echo "🚀 Setting up Azure OpenAI Streamlit Chat App..."

# Check if we're in the right directory
if [ ! -f "src/chat.py" ]; then
    echo "❌ Error: Please run this script from the streamlit-chat-app directory"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements-streamlit.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "� Creating .env file from template..."
    cp .env.example .env
    echo "   Please edit .env and add your Azure OpenAI configuration."
fi

# Check for environment variables
if [ -z "$AZURE_OPENAI_ENDPOINT" ]; then
    echo ""
    echo "⚠️  Warning: AZURE_OPENAI_ENDPOINT environment variable not set"
    echo "   Please set it with your Azure OpenAI endpoint:"
    echo "   export AZURE_OPENAI_ENDPOINT=\"https://your-resource.cognitiveservices.azure.com/\""
    echo ""
    echo "   Or add it to .env file or .streamlit/secrets.toml"
    echo ""
fi

if [ -z "$AZURE_OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: AZURE_OPENAI_API_KEY environment variable not set"
    echo "   Please set it with your Azure OpenAI API key:"
    echo "   export AZURE_OPENAI_API_KEY=\"your-api-key-here\""
    echo ""
    echo "   Or add it to .env file or .streamlit/secrets.toml"
    echo ""
fi

echo "✅ Setup complete!"
echo ""
echo "To run the application:"
echo "   streamlit run src/chat.py"
echo ""
echo "Make sure you have:"
echo "   1. Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY"
echo "   2. Deployed models in your Azure OpenAI resource"
echo "   3. Updated AVAILABLE_MODELS list to match your deployments"
import click
import requests
from bs4 import BeautifulSoup
from anthropic import Anthropic, APIError

@click.command()
@click.argument("url", type=click.STRING, required=True, metavar="<URL>")
@click.option("--max-length", default=150, help="Maximum length of the summary (default 150)", type=int)
@click.option("--api-key", envvar="ANTHROPIC_API_KEY", help="Anthropic API key (or set ANTHROPIC_API_KEY)")
@click.option("--model", envvar="ANTHROPIC_MODEL", default="claude-3-5-sonnet-latest", help="Anthropic Model to use (or set ANTHROPIC_MODEL)\nsee https://docs.anthropic.com/en/docs/about-claude/models")
@click.version_option(version="1.0.0")
def cli(url, max_length, api_key, model):
    """Summarizes a web page using the Claude API"""
    try:
        # Fetch the web page
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main text content
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])

        # Initialize the Anthropic client
        client = Anthropic(api_key=api_key)

        # Generate the summary using Claude API
        message = client.messages.create(
            model=model,
            max_tokens=max_length * 4,  # Rough estimate, adjust as needed
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following text in about {max_length} words:\n\n{text}"
                }
            ]
        )

        # Print the summary
        click.echo("Summary:")
        click.echo(message.content[0].text)
        
    except requests.RequestException as e:
        click.echo(f"Error fetching the web page: {str(e)}", err=True)
    except APIError  as e:
        click.echo(f"Error with Claude API: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}", err=True)

if __name__ == "__main__":
    cli()
    
'''
import click
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

@click.command()
@click.argument(
    "url",
    type=click.STRING,
    required=True,
    metavar="<URL>",
)
@click.option(
    "--max-length",
    default=150,
    help="Maximum length of the summary",
    type=int,
)
@click.option(
    "--min-length",
    default=50,
    help="Minimum length of the summary",
    type=int,
)
@click.version_option(version="1.0.0")
def cli(url, max_length, min_length):
    """Summarizes a web page using an LLM"""
    try:
        # Fetch the web page
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main text content
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])

        # Initialize the summarization pipeline
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        # Generate the summary
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

        # Print the summary
        click.echo("Summary:")
        click.echo(summary)

    except requests.RequestException as e:
        click.echo(f"Error fetching the web page: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}", err=True)

if __name__ == "__main__":
    cli()
'''
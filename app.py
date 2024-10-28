from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Define custom data for each tile, with hyperlinks in the 'link' key
    tiles = [
        {"title": "Request a Feature", "content": "Enter as much detail as possible", "link": "https://example.com/request-feature"},
        {"title": "Architectural Spike", "content": "Confluence Document Link", "link": "https://example.com/architectural-spike"},
        {"title": "Developer Spike Notes", "content": "Confluence Document Link", "link": "https://example.com/developer-spike-notes"},
        {"title": "Feature Breakdown", "content": "JIRA Issue Links", "link": "https://example.com/feature-breakdown"},
        {"title": "Code Changes", "content": "Merge Request Links", "link": "https://example.com/code-changes"},
        {"title": "Code Review", "content": "Review Code changes and fix issues", "link": "https://example.com/code-review"},
        {"title": "Unit Test Cases", "content": "Merge Request Link for Unit Test Cases", "link": "https://example.com/unit-test-cases"},
        {"title": "CI/CD Pipeline", "content": "Run CI/CD Pipeline", "link": "https://example.com/ci-cd-pipeline"},
        {"title": "Redeploy", "content": "Merge Changes and Redeploy App", "link": "https://example.com/redeploy"},
    ]
    return render_template('home.html', tiles=tiles)

if __name__ == '__main__':
    app.run(debug=True)

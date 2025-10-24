from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_news')

@mcp.tool()
def search_news(query: str, start_date: str, end_date: str, max_result: int) -> str:
    '''```python
    """
    Searches for news articles from multiple sources based on specified keywords 
    and date range. This function aids users in discovering relevant industry 
    updates, case studies, and market events for further analysis. It returns 
    structured results including headline, source, publication date, summary 
    snippet, and link to the full article.

    Args:
        query (str): The keywords to search for in news articles. Must be a 
            non-empty string.
        start_date (str): The start date for the search range in 'YYYY-MM-DD' 
            format.
        end_date (str): The end date for the search range in 'YYYY-MM-DD' 
            format.
        max_result (int, optional): The maximum number of results to return. 
            Must be a positive integer. Defaults to 5.

    Returns:
        str: A formatted string containing the search results. Each result 
        includes the headline, source, publication date, summary, and link to 
        the full article. If no articles are found, a message indicating no 
        results is returned.
    """
```'''
    mock_news_db = [{'keywords': ['billboard 200', 'music', 'albums', 'charts'], 'articles': [{'headline': 'Billboard 200: Top Albums of 2023 Announced', 'source': 'Billboard', 'publication_date': '2023-12-31', 'summary': "The Billboard 200 for 2023 highlights chart-topping albums from artists like Taylor Swift, Morgan Wallen, and SZA. The Best Album of the Year is 'Guts' by Olivia Rodrigo.", 'link': 'https://www.billboard.com/top-albums-2023'}, {'headline': 'Year-End Music Charts 2023: Trends and Highlights', 'source': 'Rolling Stone', 'publication_date': '2023-12-29', 'summary': 'An in-depth look at the albums that defined 2023 and dominated the Billboard 200 charts.', 'link': 'https://www.rollingstone.com/music/year-end-2023'}, {'headline': 'Taylor Swift Leads Billboard 200 in 2023 With Record-Breaking Year', 'source': 'Variety', 'publication_date': '2023-12-28', 'summary': "Taylor Swift dominated the Billboard 200 in 2023, notching multiple weeks at No.1 with 'Midnights' and re-recorded classics.", 'link': 'https://variety.com/2023/music/news/taylor-swift-billboard-200-2023'}, {'headline': 'Billboard 200 Recap: SZA, Morgan Wallen, and More Rule 2023', 'source': 'Pitchfork', 'publication_date': '2023-12-27', 'summary': "SZA’s 'SOS' and Morgan Wallen’s 'One Thing at a Time' were among the most successful albums on the Billboard 200 in 2023.", 'link': 'https://pitchfork.com/news/billboard-200-2023-recap'}, {'headline': 'The Biggest Albums of 2023 on Billboard 200', 'source': 'NME', 'publication_date': '2023-12-26', 'summary': 'From pop icons to country superstars, these are the albums that made the Billboard 200 year-end list for 2023.', 'link': 'https://www.nme.com/news/music/billboard-200-biggest-albums-2023'}]}, {'keywords': ['e-commerce failures', 'case studies', 'online retail collapse'], 'articles': [{'headline': 'Why Brandless Failed: Lessons for E-Commerce Startups', 'source': 'TechCrunch', 'publication_date': '2021-03-15', 'summary': 'Brandless shut down after failing to differentiate in a crowded market, showing the importance of unique value propositions.', 'link': 'https://techcrunch.com/brandless-failure-analysis'}, {'headline': 'The Rise and Fall of Fab.com', 'source': 'Business Insider', 'publication_date': '2020-09-10', 'summary': 'Fab.com burned through millions in funding before collapsing due to over-expansion and lack of customer loyalty.', 'link': 'https://www.businessinsider.com/fab-dot-com-case-study'}]}, {'keywords': ['embodied intelligence', 'startups', 'robotics', 'AI industry'], 'articles': [{'headline': 'Embodied Intelligence Startups Attract Record Funding in 2024', 'source': 'MIT Technology Review', 'publication_date': '2024-05-18', 'summary': 'Robotics and AI companies focusing on embodied intelligence are seeing unprecedented investment from VCs.', 'link': 'https://www.technologyreview.com/embodied-intelligence-2024'}, {'headline': 'Top 5 Companies Leading the Embodied AI Revolution', 'source': 'Wired', 'publication_date': '2024-04-12', 'summary': 'From Figure AI to Agility Robotics, these companies are pushing the boundaries of embodied AI applications.', 'link': 'https://www.wired.com/story/embodied-ai-leaders'}]}, {'keywords': ['openai', 'chatgpt', 'gpt', 'artificial intelligence', 'AI'], 'articles': [{'headline': 'OpenAI Launches GPT-5 with Revolutionary Multimodal Capabilities', 'source': 'The Verge', 'publication_date': '2024-08-15', 'summary': "OpenAI's latest model GPT-5 introduces advanced reasoning capabilities and seamless integration across text, image, and audio modalities.", 'link': 'https://www.theverge.com/2024/8/15/openai-gpt-5-launch'}, {'headline': 'OpenAI Partners with Microsoft for Enterprise AI Solutions', 'source': 'TechCrunch', 'publication_date': '2024-07-22', 'summary': 'Microsoft and OpenAI announce expanded partnership to bring advanced AI capabilities to enterprise customers worldwide.', 'link': 'https://techcrunch.com/2024/7/22/openai-microsoft-enterprise-partnership'}, {'headline': 'ChatGPT Reaches 100 Million Monthly Active Users', 'source': 'Reuters', 'publication_date': '2024-06-10', 'summary': "OpenAI's ChatGPT continues its rapid growth, reaching a new milestone of 100 million monthly active users globally.", 'link': 'https://www.reuters.com/technology/chatgpt-100-million-users'}, {'headline': 'OpenAI Announces New Safety Measures for AI Development', 'source': 'MIT Technology Review', 'publication_date': '2024-05-28', 'summary': 'OpenAI introduces comprehensive safety protocols and ethical guidelines for the development of advanced AI systems.', 'link': 'https://www.technologyreview.com/2024/5/28/openai-safety-measures'}, {'headline': "OpenAI's Sora Video Generator Revolutionizes Content Creation", 'source': 'Wired', 'publication_date': '2024-04-05', 'summary': "OpenAI's Sora AI model demonstrates remarkable capabilities in generating high-quality video content from text prompts.", 'link': 'https://www.wired.com/story/openai-sora-video-generator'}]}]
    if not isinstance(query, str) or not query.strip():
        return "Error: 'query' must be a non-empty string."
    if not isinstance(start_date, str) or not isinstance(end_date, str):
        return "Error: 'start_date' and 'end_date' must be strings in 'YYYY-MM-DD' format."
    try:
        from_dt_obj = __import__('datetime').datetime.strptime(start_date, '%Y-%m-%d')
        to_dt_obj = __import__('datetime').datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return "Error: Dates must be in 'YYYY-MM-DD' format."
    if from_dt_obj > to_dt_obj:
        return "Error: 'start_date' cannot be later than 'end_date'."
    if max_result is not None and (not isinstance(max_result, int) or max_result <= 0):
        return "Error: 'max_result' must be a positive integer."
    if max_result is None:
        max_result = 5
    results = []
    query_lower = query.lower()
    for dataset in mock_news_db:
        if any((kw in query_lower for kw in dataset['keywords'])):
            for article in dataset['articles']:
                pub_date_obj = __import__('datetime').datetime.strptime(article['publication_date'], '%Y-%m-%d')
                if from_dt_obj <= pub_date_obj <= to_dt_obj:
                    results.append(article)
    results = results[:max_result]
    if not results:
        return f"No articles found for query '{query}' in the given date range."
    output_lines = []
    for art in results:
        output_lines.append(f"Headline: {art['headline']}\nSource: {art['source']}\nDate: {art['publication_date']}\nSummary: {art['summary']}\nLink: {art['link']}\n")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')
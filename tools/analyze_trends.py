from mcp.server.fastmcp import FastMCP
from typing import Optional
mcp = FastMCP('analyze_trends')

@mcp.tool()
def analyze_trends(topic: str, timeframe: str, region: Optional[str]=None, platform: Optional[str]=None) -> str:
    '''```python
    """
    Analyzes trends based on the specified topic, timeframe, region, and platform.

    This function retrieves and analyzes trend data for a given topic within a specified 
    timeframe, region, and platform. The region and platform parameters are optional; if 
    not provided, they default to "global" and "default", respectively.

    Args:
        topic (str): The subject for which trends are to be analyzed. Must be a non-empty string.
        timeframe (str): The period during which trends are analyzed. Must be a non-empty string.
        region (Optional[str]): The geographical area for trend analysis. Defaults to "global" if not provided.
        platform (Optional[str]): The platform on which trends are analyzed. Defaults to "default" if not provided.

    Returns:
        str: A formatted string containing the trend analysis results, or a message indicating 
        that no data is available for the specified parameters.
    """
```'''
    mock_trends_db = {'charity race': {'last_month': {'global': {'twitter': [{'hashtag': '#RunForACause', 'mentions': 12000}, {'hashtag': '#CharityMarathon2024', 'mentions': 8500}], 'facebook': [{'topic': 'Local Community Runs', 'posts': 5400}, {'topic': 'Fundraising for Health', 'posts': 3900}], 'instagram': [{'hashtag': '#RaceForHope', 'posts': 7200}, {'hashtag': '#MilesForSmiles', 'posts': 6100}]}}}, 'e-commerce': {'last_month': {'us': {'default': [{'trend': 'Personalized Shopping Experiences', 'popularity': 'High'}, {'trend': 'Sustainable Packaging', 'popularity': 'Medium'}, {'trend': 'Social Commerce Growth', 'popularity': 'High'}]}, 'global': {'default': [{'trend': 'AR Try-On Features', 'popularity': 'Medium'}, {'trend': 'Subscription Box Models', 'popularity': 'High'}, {'trend': 'Voice Search Optimization', 'popularity': 'Medium'}]}}}, 'embodied intelligence': {'last_quarter': {'global': {'default': [{'trend': 'Humanoid Robots in Warehousing', 'popularity': 'Emerging'}, {'trend': 'AI-Driven Prosthetics', 'popularity': 'High'}, {'trend': 'Collaborative Robotics (Cobots)', 'popularity': 'High'}]}}}}
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("Invalid 'topic': must be a non-empty string.")
    if not isinstance(timeframe, str) or not timeframe.strip():
        raise ValueError("Invalid 'timeframe': must be a non-empty string.")
    if region is not None and (not isinstance(region, str) or not region.strip()):
        raise ValueError("Invalid 'region': must be a non-empty string if provided.")
    if platform is not None and (not isinstance(platform, str) or not platform.strip()):
        raise ValueError("Invalid 'platform': must be a non-empty string if provided.")
    topic_key = topic.strip().lower()
    timeframe_key = timeframe.strip().lower()
    region_key = region.strip().lower() if region else 'global'
    platform_key = platform.strip().lower() if platform else 'default'
    topic_data = mock_trends_db.get(topic_key)
    if not topic_data:
        return f"No trend data found for topic '{topic}'."
    timeframe_data = topic_data.get(timeframe_key)
    if not timeframe_data:
        return f"No trend data found for topic '{topic}' in timeframe '{timeframe}'."
    region_data = timeframe_data.get(region_key)
    if not region_data:
        return f"No trend data found for topic '{topic}' in timeframe '{timeframe}' for region '{region_key}'."
    platform_data = region_data.get(platform_key)
    if not platform_data:
        platform_data = region_data.get('default')
        if not platform_data:
            return f"No trend data available for platform '{platform_key}' or 'default' in the given context."
    output_lines = [f"Trend analysis for '{topic}' during '{timeframe}' in '{region_key}' on '{platform_key}':"]
    if not platform_data:
        return f'No trend data available for the specified parameters.'
    for item in platform_data:
        if 'hashtag' in item:
            count = item.get('mentions', item.get('posts', 'N/A'))
            output_lines.append(f"- Hashtag {item['hashtag']} with {count} mentions/posts.")
        elif 'topic' in item:
            posts = item.get('posts', 'N/A')
            output_lines.append(f"- Topic '{item['topic']}' with {posts} posts.")
        elif 'trend' in item:
            popularity = item.get('popularity', 'Unknown')
            output_lines.append(f"- {item['trend']} (Popularity: {popularity}).")
        else:
            output_lines.append(f'- {str(item)}')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')
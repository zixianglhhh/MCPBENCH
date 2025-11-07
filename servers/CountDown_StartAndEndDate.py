from mcp.server.fastmcp import FastMCP
mcp = FastMCP('CountDown_StartAndEndDate')

@mcp.tool()
def CountDown_StartAndEndDate(Ele: str, StartDate: str, EndDate: str, EndFunc: str=None) -> str:
    '''```python
"""
Creates a customizable countdown timer between a defined start and end date.

This function initializes a countdown timer that tracks the time remaining between a specified start date and end date. It updates a target element with the remaining time and can optionally trigger a callback function when the countdown ends. This is useful for creating timers for vocabulary sessions, timed quizzes, or any time-limited activities.

Args:
    Ele (str): The identifier of the target element where the countdown will be displayed. Must be a non-empty string representing the DOM element or component.
    StartDate (str): The start date and time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS). The countdown begins when this time is reached.
    EndDate (str): The end date and time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS). The countdown ends when this time is reached. Must be later than StartDate.
    EndFunc (str, optional): A callback function to execute when the countdown ends. Can be None if no callback is needed.

Returns:
    str: A status message indicating the result of the countdown creation. Possible messages include:
         - "Countdown scheduled to start at {StartDate}" if the current time is before the start time.
         - "Countdown running: {seconds} seconds remaining" if the countdown is currently active.
         - "Countdown already ended." if the end time has passed.
         - Error messages for invalid parameters or date formats.

Raises:
    ValueError: If Ele is not a valid string, if the dates are in an invalid format, or if EndDate is not later than StartDate.
"""
```'''
    mock_countdowns_db = {}
    if not Ele or not isinstance(Ele, str):
        return 'Error: Invalid Ele parameter. Must be a non-empty string representing target element.'
    if not StartDate or not isinstance(StartDate, str):
        return "Error: Invalid StartDate parameter. Must be a date string in format 'YYYY-MM-DDTHH:MM:SS'."
    if not EndDate or not isinstance(EndDate, str):
        return "Error: Invalid EndDate parameter. Must be a date string in format 'YYYY-MM-DDTHH:MM:SS'."
    from datetime import datetime
    try:
        start_dt = datetime.fromisoformat(StartDate)
        end_dt = datetime.fromisoformat(EndDate)
    except ValueError:
        return 'Error: StartDate or EndDate is not in a valid ISO date format.'
    if end_dt <= start_dt:
        return 'Error: EndDate must be after StartDate.'
    now = datetime.now()
    if now < start_dt:
        countdown_status = 'Countdown scheduled to start at {}'.format(StartDate)
    elif start_dt <= now < end_dt:
        remaining = end_dt - now
        countdown_status = 'Countdown running: {} seconds remaining'.format(int(remaining.total_seconds()))
    else:
        countdown_status = 'Countdown already ended.'
        if EndFunc and EndFunc.strip():
            # Since EndFunc is now a string, we'll just log that it would be called
            return f'Countdown ended. EndFunc callback "{EndFunc}" would be executed.'
        return 'Countdown not created because end time has already passed.'
    mock_countdowns_db[Ele] = {'start': StartDate, 'end': EndDate, 'status': countdown_status, 'callback_set': bool(EndFunc and EndFunc.strip())}
    if Ele.lower().startswith('vocab_timer'):
        return f"Vocabulary session countdown created for element '{Ele}'. {countdown_status}"
    return f"Countdown created for element '{Ele}'. {countdown_status}"
if __name__ == '__main__':
    mcp.run(transport='stdio')
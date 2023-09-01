import json
from datetime import datetime
from github import Github
from dateutil.relativedelta import relativedelta

# Read configuration from JSON file
with open("gh-params.json", "r") as config_file:
    config = json.load(config_file)

github_access_token = config.get("github_access_token", "")
repository_name = config.get("repository_name", "")
months_ago = config.get("months_ago", 3)
author_logins = config.get("author_logins", [])

# Initialize the GitHub API client
g = Github(github_access_token)

# Lists to store time differences for each PR
time_differences = []

# Get the repository
repo = g.get_repo(repository_name)

# Calculate the date cutoff (months ago)
cutoff_date = datetime.now().replace(day=1) - relativedelta(months=months_ago)

# Find and analyze PRs for specified authors
for author_login in author_logins:
    # Get all PRs for the repository
    all_prs = repo.get_pulls(state="closed", sort="created", direction="asc")

    # Filter PRs created by the specified author
    author_prs = [
        pr
        for pr in all_prs
        if pr.user.login == author_login and pr.created_at >= cutoff_date
    ]

    for pr in author_prs:
        # Check if the PR has comments
        comments = pr.get_review_comments()
        first_comment = None

        # Find the first comment on the PR
        for comment in comments:
            if not first_comment or comment.created_at < first_comment.created_at:
                first_comment = comment

        if first_comment:
            # Calculate the time difference
            pr_created_at = pr.created_at
            first_comment_created_at = first_comment.created_at
            time_difference = first_comment_created_at - pr_created_at
            time_differences.append(time_difference.total_seconds())

# Calculate the average time difference
if time_differences:
    average_time = sum(time_differences) / len(time_differences)
    hours, remainder = divmod(average_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"Average time taken between PR creation and first comment for specified authors: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    )
else:
    print(
        "No comments found on PRs by the specified authors within the specified time range."
    )

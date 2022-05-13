def get_mysql_insert_query(category):
    """
    Retrieve the mysql query to use.

    :param category: The category to apply. 0 for "issue" and 1 for "pull_request".
    :return: The selected MySQL query.
    """
    if category == 1:
        return """INSERT INTO pull_request (
                            pull_request_id, title, url, created_at, number, body, closed_at, comments, comments_url, 
                            labels, pull_request, state, commits, additions, deletions, changed_files, 
                            commits_data, updated_at
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    else:
        return """INSERT INTO issue (
                            issue_id, title, url, created_at, number, body, closed_at, comments, comments_url, labels,
                            pull_request, state, commits, additions, deletions, changed_files, commits_data, updated_at
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

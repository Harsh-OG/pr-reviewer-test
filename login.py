@router.get("/github/{owner}/{repo}/pulls/{pr_number}")
async def read_pull_request(
    owner: str,
    repo: str,
    pr_number: int
):
    result = await fetch_pull_request(
        owner,
        repo,
        pr_number
    )

    return result

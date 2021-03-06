generate_post_data()
{
  cat <<EOF
{
  "body": "$(cat gh-pr-comment.log | sed -z 's/\n/\\n/g')"
}
EOF
}
PR_NUMBER=$(echo $GITHUB_REF | awk 'BEGIN { FS = "/" } ; { print $3 }')
echo "github ref:" $GITHUB_REF
echo "pr number:" $PR_NUMBER
echo "PR number" "${PR_NUMBER2}"
echo "PR number"  "${PR_NUMBER}"
echo "github_repository:" "$GITHUB_REPOSITORY"

PR_NUMBER=$(jq --raw-output .pull_request.number "$GITHUB_EVENT_PATH")
echo PR_NUMBER
#PR_NUMBER="${PR_NUMBER2}"
curl -s -H "Authorization: token ${KEY4HEP_COMMENT_BOT_TOKEN}" \
 -X POST -d "$(generate_post_data)"  \
 "https://api.github.com/repos/${GITHUB_REPOSITORY}/issues/${PR_NUMBER}/comments"


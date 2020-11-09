# Update Connect Posts from a resources.json file

Currently, during Connect, a resources.json file is updated to ensure resources are available as soon as possible. These are hosted at https://static.linaro.org/connect/{{connect_code}}/resources.json

This script fetches the resources data from the provided URL and then loops over the posts in the connect.linaro.org website repo, adding the following front matter fields:

```yaml
amazon_s3_presentation_url: https://static.linaro.org/..... # "" if not URL exists in resources.json
amazon_s3_video_url: https://static.linaro.org/..... # "" if not URL exists in resources.json
```

Clone this repository:

```bash
git clone git@github.com:linaro-marketing/export_connect_resources_json_to_frontmatter.git
```

`cd` into the directory:

```bash
cd export_connect_resources_json_to_frontmatter
```

Run the `connect_posts_resources_updater.py` script over your posts directory for a clean start! Provide the full path to your `_posts` directory and to your new allowed tags:

```bash
python3 connect_posts_resources_updater.py /home/god/Git/connect.linaro.org/_posts/lvc20/ https://static.linaro.org/connect/lvc20/resources.json
```

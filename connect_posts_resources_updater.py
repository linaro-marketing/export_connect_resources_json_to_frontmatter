import frontmatter
import os
import re
import argparse
import requests 

parser = argparse.ArgumentParser(description='Add links to resources stored in a resources.json file to the front matter for the relevant posts.')
parser.add_argument('posts', metavar='P', help='The full path to your posts root. All subdirectories are included.')
parser.add_argument('resources_json', metavar='R', help='Path to the resources.json file on S3')
args = parser.parse_args()

def get_resources(resources_url):
    r = requests.get(url=resources_url)
    return r.json()

def update_posts(root, resources_data):
    file_list = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith((".markdown", ".md")):
                file_list.append(os.path.join(path, name))
    # Open each markdown file found and get the current list of tags
    for file in file_list:
        print("Processing {}...".format(file))
        post = frontmatter.load(file)
        if "session_id" in post:
            session_id = post["session_id"]
            for resource in resources_data:
                if resource["session_id"].lower() == session_id.lower():
                    if len(resource["s3_presentation_url"]) > 0:
                        post["amazon_s3_presentation_url"] =  resource["s3_presentation_url"][0]
                    else:
                        post["amazon_s3_presentation_url"] = ""
                    if resource["s3_video_url"] != "":
                        post["amazon_s3_video_url"] =  resource["s3_video_url"]
                    else:
                        post["amazon_s3_video_url"] =  ""
        # write new tags to file
        with open(file, "w+") as new_post_file:
            new_post_file.writelines(frontmatter.dumps(post, sort_keys=False))


if __name__ == "__main__":
    resources_data = get_resources(args.resources_json)
    replaced = update_posts(args.posts, resources_data)
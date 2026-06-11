# Module 7 Lesson 6: After-Class Project
# Project Name: Web Traffic Router Query Parameter Extraction Matrix

import re

class WebURLRouteParser:
    def extract_query_dictionary(self, complete_url_string):
        # Capture standard tracking parameters inside HTTP GET routing lines
        parameter_pairs_list = re.findall(r'[?&]([^=&#]+)=([^&#]*)', complete_url_string)
        return {key: value for key, value in parameter_pairs_list}

if __name__ == "__main__":
    parser = WebURLRouteParser()
    url = "https://ioi.algorithms.edu/dashboard?user=rohan_99&token=0a4f5b&session=active"
    print(f"Extracted Parameter Context Map: {parser.extract_query_dictionary(url)}")
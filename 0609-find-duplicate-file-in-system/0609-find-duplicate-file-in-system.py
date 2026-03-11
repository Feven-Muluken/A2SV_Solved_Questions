from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)
        
        for path in paths:
            parts = path.split()
            directory = parts[0]
            
            for file_data in parts[1:]:
                content_start = file_data.index('(')
                file_name = file_data[:content_start]
                content = file_data[content_start+1:-1]
                
                content_map[content].append(f"{directory}/{file_name}")
        
        return [files for files in content_map.values() if len(files) > 1]
import os
import glob
import psutil

inputFolder = 'input'
outputFolder = 'output'

class demucs:
    extensions = ['mp3', 'wav', 'flac']
    
    def __init__(self):
        self.CPU = str(psutil.cpu_count() * 2)
        print(self.CPU)
    
    def separate(self, level, only):
        if level == 'high':
            model = ' mdx_extra '
            freq = ' --float32'
        elif level == 'low':
            model = ' mdx_extra_q '
            freq = ' --int24'
        
        fileList = self.findFiles()
        
        for file in fileList:
            print(file)
            cmd = 'demucs tracks ' + file
            cmd += ' -n ' + model
            cmd += ' -j ' + self.CPU
            cmd += freq
            cmd += ' -o ' + outputFolder
            if only is not None:
                cmd += ' --two-stems ' + only
                            
            print(cmd)
            # os.system(cmd)
    
    def findFiles(self):
        fileList = []
        for format in self.extensions:
            for name in glob.glob('./' + inputFolder + '/*.' + format):
                # name = name.lstrip("./" + inputFolder + '/')
                fileList.append(name)
        
        # print(fileList)
        return fileList


if __name__=='__main__':
    dm = demucs()
    dm.separate('high', 'vocals')
    dm.separate('low', 'vocals')
    dm.separate('low', 'bass')
    
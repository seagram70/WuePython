import glob
import os
import DocStatistic.DocStatistikVDFS


def wait4Files(path, filename, Y, year, jul, pattern):
    for name in glob.glob(path + filename + Y + year + jul + pattern):
        print (name)
        for name1 in glob.glob(DeltaFake + filename + Y + year + jul + pattern):
            print (name1)
            if os.path.exists(name1):
                return False
        with open(path + filename + Y + year + jul + pattern) as f:
            line_count = len(f.readlines())
            print (line_count)
            out = open(StatDir + StatFile, 'a')
            out.write(today + "  " + hms + "   " + "RUN" + pattern + "  Docs in File " + "  " + (str(line_count)) + "\n")
            out.close()
            logger.info('The Docs are counted and writied to the File ' + StatDir + StatFile + '.')

            sendEmail(server + "@six-group.com", 'heinz.wuethrich@six-group.com', 
#            "Docstatistic VDFS " + environment, today + "     RUN" + pattern + "   " + (str(line_count)) + " Docs", files=[])
            "Docstatistic VDFS " + environment, pattern + "  " + (str(line_count)) + " Docs", files=[])
            s1 = open(DeltaFake + filename + Y + year + jul + pattern, 'w')
            s1.close()
            
            inputFile = filename + Y + year + jul + pattern
            logger.info('call subprocess DocCounter.py with the inputFilename ' + inputFile + '.')
            subprocess.call(['python.exe', 'DocCounter.py', inputFile])
        return True
    return False
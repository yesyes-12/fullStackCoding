#from extractors.indeed import extract_indeed_jobs
from extractors.remoteok import extract_remoteok_jobs
from file import save_to_file

keyword = input("What do you want to search for? ")

remoteok = extract_remoteok_jobs(keyword)

save_to_file(keyword, remoteok)
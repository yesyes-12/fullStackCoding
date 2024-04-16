def save_to_file(filename, jobs):
    file = open(f"{filename}.csv", mode="w", encoding="utf-8", newline = "")
    file.write("Title, Company, Location, Link\n")
    
    for job in jobs:
        file.write(f"{job['title']}, {job['company']}, \
            {job['location']}, {job['link']}\n")
        
    file.close()
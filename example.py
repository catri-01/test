import psutil
import os

# def git_operation():
#  print("I am adding example.py file to the remote repository.")


def get_disk_usage():
    
    disk_usage = psutil.disk_io_counters()
    return disk_usage.read_count, disk_usage.write_count

def main():
   read_count, write_count = get_disk_usage()

   print(f"Opérations de lecture sur le disque: {read_count} ")
   print(f"Opérations de lecture sur le disque: {write_count} ")

# disk_usage = get_disk_usage()
# print(disk_usage)



if __name__ == "__main__":
    main()

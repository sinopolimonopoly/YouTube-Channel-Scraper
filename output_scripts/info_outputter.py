# Outputs videos dictionary to console
def output_info(video_dict):

    # Header
    print(f"{'Video ID':<15} {'Title':<100} {'Upload Date':<15} {'Duration':<13} {"Duration in s":<18} {'View Count':<10} {'Like Count':<10} {'Comment Count':<13}")

    # Rows
    for k, v in video_dict.items():
        # F strings are a nice way to continue long lines of code in multiple lines
        print(
                f"{k:<15} {v["Title"]:<100} {v["Upload Date"]:<15} {v["Duration"]:<13} {v["Duration in s"]:<18} "
                f"{v["View Count"]:<10} {v["Like Count"]:<10} {v["Comment Count"]:<13}" 
            )
        
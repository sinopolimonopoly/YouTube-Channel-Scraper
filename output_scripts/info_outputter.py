def output_info(video_dict):

    print(f"{'Video ID':<15} {'Title':<80} {'Upload Date':<15} {'Duration':<13} {"Duration in s":<18} {'View Count':<10} {'Like Count':<10} {'Comment Count':<10}")

    for k, v in video_dict.items():
        print(
                f"{k:<15} {v["Title"]:<80} {v["Upload Date"]:<15} {v["Duration"]:<13} {v["Duration in s"]:<18} "
                f"{v["View Count"]:<10} {v["Like Count"]:<10} {v["Comment Count"]:<10}" 
            )
        
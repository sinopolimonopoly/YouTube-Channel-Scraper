def output_info(video_info, max_duration):

    if max_duration:
        print(f"{'Video ID':<15} {'Title':<80} {'Upload Date':<15} {'Raw Duration':<13} {'Duration in S':<13} {'View Count':<10} {'Like Count':<10} {'Comment Count':<10}")

        for k, v in video_info.items():
            print(
                    f"{k:<15} {v["Information"]["Title"]:<80} {v["Information"]["Upload Date"]:<15} {v["Information"]["Duration"]["min_sec"]:<13} "
                    f"{v["Information"]["Duration"]["secs"]:<13} {v["Statistics"]["View Count"]:<10} {v["Statistics"]["Like Count"]:<10} {v["Statistics"]["Comment Count"]:<10}" 
                )
    else:
        print(f"{'Video ID':<15} {'Title':<80} {'Upload Date':<15} {'Duration':<13} {'View Count':<10} {'Like Count':<10} {'Comment Count':<10}")

        for k, v in video_info.items():
            print(
                    f"{k:<15} {v["Information"]["Title"]:<80} {v["Information"]["Upload Date"]:<15} {v["Information"]["Duration"]:<13} "
                    f"{v["Statistics"]["View Count"]:<10} {v["Statistics"]["Like Count"]:<10} {v["Statistics"]["Comment Count"]:<10}" 
                )

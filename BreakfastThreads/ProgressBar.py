class ProgressBar:
    def display_progress_bar(self, progress):

        for i in range(0, progress, 1):
            print("██", end="")

        for i in range(0, 10 - progress, 1):
            print("░░", end="")
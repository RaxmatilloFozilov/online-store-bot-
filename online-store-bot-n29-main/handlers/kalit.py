import re

class AnnouncementBot:
    def __init__(self, announcements):
        self.announcements = announcements
        self.results_per_page = 5

    def search_announcements(self, keyword, page=1):
        keyword_pattern = re.compile(rf'\b{re.escape(keyword)}\b', re.IGNORECASE)
        matching_announcements = [announcement for announcement in self.announcements if
                                  keyword_pattern.search(announcement)]

        start_idx = (page - 1) * self.results_per_page
        end_idx = start_idx + self.results_per_page
        paginated_results = matching_announcements[start_idx:end_idx]

        return paginated_results

    def display_results(self, results):
        if results:
            for idx, announcement in enumerate(results, start=1):
                print(f"{idx}. {announcement}")
        else:
            print("No announcements found.")

    def search_and_display(self, keyword, page=1):
        results = self.search_announcements(keyword, page)
        self.display_results(results)


announcements_data = [
    "Lenovo announces new laptop series.",
    "HP releases a powerful workstation.",
    "MacBook Pro with upgraded features launched.",
    "New MacBook Air available now.",
]

bot = AnnouncementBot(announcements_data)

while True:
    user_input = input("Enter a keyword (type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    page_input = int(input("Enter page number (default is 1): ") or 1)

    bot.search_and_display(user_input, page_input)


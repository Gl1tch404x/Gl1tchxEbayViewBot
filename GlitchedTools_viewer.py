import os
import sys
import time
import random
import requests
from colorama import init, Fore, Style, Back

init(autoreset=True)

PURPLE = Fore.MAGENTA
BRIGHT_PURPLE = Fore.MAGENTA + Style.BRIGHT
BG_PURPLE = Back.MAGENTA
RESET = Style.RESET_ALL

LOGO = f"""
{BRIGHT_PURPLE}
 ██████╗ ██╗     ██╗████████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██║     ██║╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║     ██║   ██║   ██║     ███████║█████╗  ██║  ██║
██║   ██║██║     ██║   ██║   ██║     ██╔══██║██╔══╝  ██║  ██║
╚██████╔╝███████╗██║   ██║   ╚██████╗██║  ██║███████╗██████╔╝
 ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                             
████████╗ ██████╗  ██████╗ ██╗     ███████╗                  
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝                  
   ██║   ██║   ██║██║   ██║██║     ███████╗                  
   ██║   ██║   ██║██║   ██║██║     ╚════██║                  
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║                  
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                  
{RESET}
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.254",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(LOGO)
    print(f"{PURPLE}{'=' * 80}{RESET}")
    print(f"{BRIGHT_PURPLE}     Welcome to Glitched Tools eBay View Tool  | Made by: Glitched Tools     {RESET}")
    print(f"{PURPLE}{'=' * 80}{RESET}")
    print(f"{PURPLE}This tool sends real HTTP requests to eBay listings{RESET}")
    print()

def print_menu():
    print(f"{PURPLE}Main Menu:{RESET}")
    print(f"{BRIGHT_PURPLE}1.{RESET} {PURPLE}Start Sending Views{RESET}")
    print(f"{BRIGHT_PURPLE}2.{RESET} {PURPLE}Exit{RESET}")
    print()

def get_user_choice():
    while True:
        try:
            choice = input(f"{PURPLE}Enter your choice (1-2): {RESET}")
            choice = int(choice)
            if 1 <= choice <= 2:
                return choice
            else:
                print(f"{BRIGHT_PURPLE}Invalid choice. Please enter 1 or 2.{RESET}")
        except ValueError:
            print(f"{BRIGHT_PURPLE}Invalid input. Please enter a number.{RESET}")

def validate_ebay_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    ebay_domains = ["ebay.com", "ebay.co.uk", "ebay.ca", "ebay.de", "ebay.fr", "ebay.it", 
                     "ebay.es", "ebay.com.au", "ebay.at", "ebay.be", "ebay.ch", "ebay.ie"]
    
    valid_domain = any(domain in url for domain in ebay_domains)
    
    is_listing = "itm" in url or "item" in url
    
    return url if valid_domain and is_listing else None

def get_listing_url():
    while True:
        url = input(f"{PURPLE}Enter the eBay seller listing URL: {RESET}")
        validated_url = validate_ebay_url(url)
        
        if validated_url:
            return validated_url
        else:
            print(f"{BRIGHT_PURPLE}Invalid eBay listing URL. Please enter a valid URL.{RESET}")
            print(f"{PURPLE}Example: https://www.ebay.com/itm/123456789{RESET}")

def get_view_count():
    while True:
        try:
            views = input(f"{PURPLE}Enter the number of views to send (1-1000): {RESET}")
            views = int(views)
            if 1 <= views <= 1000:
                return views
            else:
                print(f"{BRIGHT_PURPLE}Invalid number. Please enter a value between 1 and 1000.{RESET}")
        except ValueError:
            print(f"{BRIGHT_PURPLE}Invalid input. Please enter a number.{RESET}")

def send_views(url, num_views):
    successful = 0
    unsuccessful = 0
    
    print(f"\n{PURPLE}Starting to send HTTP requests to the listing...{RESET}")
    print(f"{PURPLE}NOTE: These are real HTTP requests but eBay's actual view counting may differ{RESET}")
    print(f"{PURPLE}{'=' * 60}{RESET}")
    
    session = requests.Session()
    
    for i in range(num_views):
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Cache-Control": "max-age=0",
            }
            
            referrers = [
                "https://www.google.com/",
                "https://www.bing.com/",
                "https://search.yahoo.com/",
                "https://www.ebay.com/",
                "https://www.facebook.com/",
                "https://www.instagram.com/",
                None
            ]
            if random.choice([True, False]):
                headers["Referer"] = random.choice(referrers)
            
            response = session.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                successful += 1
                print(f"\r{PURPLE}Progress: [{i+1}/{num_views}] - Successful: {successful}, Unsuccessful: {unsuccessful}{RESET}", end="")
            else:
                unsuccessful += 1
                print(f"\r{PURPLE}Progress: [{i+1}/{num_views}] - Successful: {successful}, Unsuccessful: {unsuccessful}{RESET}", end="")
                
            time.sleep(random.uniform(1.0, 5.0))
            
            if i % 5 == 0:
                session.cookies.clear()
                
        except requests.exceptions.RequestException:
            unsuccessful += 1
            print(f"\r{PURPLE}Progress: [{i+1}/{num_views}] - Successful: {successful}, Unsuccessful: {unsuccessful}{RESET}", end="")
            time.sleep(random.uniform(2.0, 7.0))
            
        if (i + 1) % 10 == 0 or i == num_views - 1:
            sys.stdout.write("\033[K")
            print(f"\r{PURPLE}Progress: [{i+1}/{num_views}] - Successful: {successful}, Unsuccessful: {unsuccessful}{RESET}")
            
    return successful, unsuccessful

def show_results(successful, unsuccessful):
    total = successful + unsuccessful
    
    print(f"\n{PURPLE}{'=' * 60}{RESET}")
    print(f"{BRIGHT_PURPLE}             Results Summary                {RESET}")
    print(f"{PURPLE}{'=' * 60}{RESET}")
    print(f"{PURPLE}Total HTTP Requests Sent:{RESET} {total}")
    print(f"{PURPLE}Successful Requests:{RESET} {successful} ({successful/total*100:.1f}%)")
    print(f"{PURPLE}Failed Requests:{RESET} {unsuccessful} ({unsuccessful/total*100:.1f}%)")
    print(f"{PURPLE}{'=' * 60}{RESET}")
    print(f"{PURPLE}Note: eBay may count views differently from HTTP requests{RESET}")
    
    input(f"\n{BRIGHT_PURPLE}Press Enter to return to the main menu...{RESET}")

def main():
    try:
        while True:
            print_header()
            print_menu()
            choice = get_user_choice()
            
            if choice == 1:
                print_header()
                print(f"{BRIGHT_PURPLE}Send Views to eBay Listing{RESET}")
                print(f"{PURPLE}{'=' * 60}{RESET}\n")
                
                listing_url = get_listing_url()
                view_count = get_view_count()
                
                successful, unsuccessful = send_views(listing_url, view_count)
                show_results(successful, unsuccessful)
                
            elif choice == 2:
                clear_screen()
                print(LOGO)
                print(f"{BRIGHT_PURPLE}Thank you for using Adzz Tools!{RESET}")
                print(f"{PURPLE}Goodbye!{RESET}")
                break
    
    except KeyboardInterrupt:
        clear_screen()
        print(LOGO)
        print(f"{BRIGHT_PURPLE}Program interWrupted. Exiting...{RESET}")
        
    except Exception as e:
        clear_screen()
        print(LOGO)
        print(f"{BRIGHT_PURPLE}An unexpected error occurred: {e}{RESET}")
        print(f"{PURPLE}The application will now exit.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import os
import sys
import time
import random

class KaliCommandsTool:
    def __init__(self):
        self.commands = {
            1: {"name": "ls", "desc": "The most frequently used command in Linux to list directories"},
            2: {"name": "mkdir", "desc": "Command used to create directories in Linux"},
            3: {"name": "rm", "desc": "Delete files or directories"},
            4: {"name": "cat", "desc": "Display file contents on the terminal"},
            5: {"name": "less", "desc": "Linux command to display paged outputs in the terminal"},
            6: {"name": "whoami", "desc": "Get the active username"},
            7: {"name": "grep", "desc": "Search for a string within an output"},
            8: {"name": "diff", "desc": "Find the difference between two files"},
            9: {"name": "sort", "desc": "To sort the content of a file while outputting"},
            10: {"name": "unzip", "desc": "Unzip files in Linux"},
            11: {"name": "ps", "desc": "Display active processes"},
            12: {"name": "mount", "desc": "Mount file systems in Linux"},
            13: {"name": "ifconfig", "desc": "Display network interfaces and IP addresses"},
            14: {"name": "ufw", "desc": "Firewall command"},
            15: {"name": "sudo", "desc": "Command to escalate privileges in Linux"},
            16: {"name": "dd", "desc": "Majorly used for creating bootable USB sticks"},
            17: {"name": "whereis", "desc": "Locate the binary, source, and manual pages for a command"},
            18: {"name": "useradd and usermod", "desc": "Add new user or change existing users data"},
            19: {"name": "pwd", "desc": "Print working directory command in Linux"},
            20: {"name": "mv", "desc": "Move or rename files in Linux"},
            21: {"name": "touch", "desc": "Create blank/empty files"},
            22: {"name": "clear", "desc": "Clear the terminal display"},
            23: {"name": "man", "desc": "Access manual pages for all Linux commands"},
            24: {"name": "tar", "desc": "Command to extract and compress files in Linux"},
            25: {"name": "head", "desc": "Return the specified number of lines from the top"},
            26: {"name": "cmp", "desc": "Allows you to check if two files are identical"},
            27: {"name": "export", "desc": "Export environment variables in Linux"},
            28: {"name": "ssh", "desc": "Secure Shell command in Linux"},
            29: {"name": "kill and killall", "desc": "Kill active processes by process ID or name"},
            30: {"name": "chmod", "desc": "Command to change file permissions"},
            31: {"name": "traceroute", "desc": "Trace all the network hops to reach the destination"},
            32: {"name": "iptables", "desc": "Base firewall for all other firewall utilities to interface with"},
            33: {"name": "cal", "desc": "View a command-line calendar"},
            34: {"name": "whatis", "desc": "Find what a command is used for"},
            35: {"name": "passwd", "desc": "Update passwords"},
            36: {"name": "cd", "desc": "Linux command to navigate through directories"},
            37: {"name": "cp", "desc": "Similar usage as mv but for copying files in Linux"},
            38: {"name": "ln", "desc": "Create symbolic links (shortcuts) to other files"},
            39: {"name": "echo", "desc": "Print any text that follows the command"},
            40: {"name": "uname", "desc": "Linux command to get basic information"},
            41: {"name": "tail", "desc": "Return the specified number of lines from the bottom"},
            42: {"name": "comm", "desc": "Combines the functionality of diff and cmp"},
            43: {"name": "zip", "desc": "Zip files in Linux"},
            44: {"name": "service", "desc": "Linux command to start and stop services"},
            45: {"name": "df", "desc": "Display disk filesystem information"},
            46: {"name": "chown", "desc": "Command for granting ownership of files or folders"},
            47: {"name": "wget", "desc": "Direct download files from the internet"},
            48: {"name": "apt", "desc": "Package managers depending on the distro"},
            49: {"name": "alias", "desc": "Create custom shortcuts for your regularly used commands"},
            50: {"name": "top", "desc": "View active processes live with their system usage"}
        }
        
        self.colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "purple": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "bold": "\033[1m",
            "underline": "\033[4m",
            "end": "\033[0m"
        }
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        banner = f"""
{self.colors['green']}
 ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ██╗  ██╗███████╗██████╗ ███████╗███████╗
 ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ██║  ██║██╔════╝██╔══██╗██╔════╝██╔════╝
    ██║   ██║   ██║██║   ██║██║     █████╗      ███████║█████╗  ██████╔╝█████╗  █████╗  
    ██║   ██║   ██║██║   ██║██║     ██╔══╝      ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  
    ██║   ╚██████╔╝╚██████╔╝███████╗███████╗    ██║  ██║███████╗██║  ██║███████╗███████╗
    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                        
{self.colors['cyan']}
                    ██████╗██╗  ██╗ ██████╗ ██╗    ██╗██╗   ██╗██████╗ ██████╗ ███████╗██████╗ ██╗   ██╗
                   ██╔════╝██║  ██║██╔═══██╗██║    ██║██║   ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗╚██╗ ██╔╝
                   ██║     ███████║██║   ██║██║ █╗ ██║██║   ██║██████╔╝██████╔╝█████╗  ██████╔╝ ╚████╔╝ 
                   ██║     ██╔══██║██║   ██║██║███╗██║██║   ██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗  ╚██╔╝  
                   ╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝╚██████╔╝██║  ██║██║  ██║███████╗██║  ██║   ██║   
                    ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                                                                         
{self.colors['yellow']}
                           KALI LINUX COMMANDS CHEAT SHEET TOOL
{self.colors['end']}
"""
        print(banner)
    
    def print_typing_effect(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_colored_text(self, text, color):
        return f"{self.colors[color]}{text}{self.colors['end']}"
    
    def display_all_commands(self):
        self.clear_screen()
        self.print_banner()
        
        print(self.print_colored_text("=" * 80, "cyan"))
        print(self.print_colored_text("                     COMPLETE KALI LINUX COMMANDS LIST", "yellow"))
        print(self.print_colored_text("=" * 80, "cyan"))
        print()
        
        for i in range(1, 51):
            cmd = self.commands[i]
            color = random.choice(["green", "yellow", "cyan", "white"])
            print(f"{self.print_colored_text(f'{i:2d}.', 'purple')} {self.print_colored_text(cmd['name'], color)} - {cmd['desc']}")
            
            if i % 10 == 0:
                print()
                input(self.print_colored_text("Press Enter to continue...", "yellow"))
                self.clear_screen()
                self.print_banner()
                print(self.print_colored_text("=" * 80, "cyan"))
                print(self.print_colored_text("                     COMPLETE KALI LINUX COMMANDS LIST", "yellow"))
                print(self.print_colored_text("=" * 80, "cyan"))
                print()
    
    def search_command(self, query):
        results = []
        for num, cmd in self.commands.items():
            if query.lower() in cmd['name'].lower() or query.lower() in cmd['desc'].lower():
                results.append((num, cmd))
        return results
    
    def display_command_details(self, command_num):
        if command_num in self.commands:
            cmd = self.commands[command_num]
            print()
            print(self.print_colored_text("=" * 60, "green"))
            print(self.print_colored_text(f"COMMAND DETAIL: {cmd['name']}", "yellow"))
            print(self.print_colored_text("=" * 60, "green"))
            print(self.print_colored_text(f"Command: ", "cyan") + self.print_colored_text(cmd['name'], "white"))
            print(self.print_colored_text(f"Description: ", "cyan") + self.print_colored_text(cmd['desc'], "white"))
            print(self.print_colored_text(f"Command Number: ", "cyan") + self.print_colored_text(str(command_num), "white"))
            print(self.print_colored_text("=" * 60, "green"))
            print()
        else:
            print(self.print_colored_text("Command not found!", "red"))
    
    def display_contact_info(self):
        print()
        print(self.print_colored_text("=" * 60, "purple"))
        print(self.print_colored_text("                   CONTACT INFORMATION", "yellow"))
        print(self.print_colored_text("=" * 60, "purple"))
        print(self.print_colored_text("Telegram ID: ", "cyan") + self.print_colored_text("https://t.me/darkvaiadmin", "green"))
        print(self.print_colored_text("Telegram Channel: ", "cyan") + self.print_colored_text("https://t.me/windowspremiumkey", "green"))
        print(self.print_colored_text("Hacking/Cracking Website: ", "cyan") + self.print_colored_text("https://crackyworld.com/", "green"))
        print(self.print_colored_text("=" * 60, "purple"))
        print()
    
    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            
            print(self.print_colored_text("=" * 60, "cyan"))
            print(self.print_colored_text("                   MAIN MENU", "yellow"))
            print(self.print_colored_text("=" * 60, "cyan"))
            print(self.print_colored_text("1. View All Commands", "green"))
            print(self.print_colored_text("2. Search Command", "yellow"))
            print(self.print_colored_text("3. Get Command Details", "cyan"))
            print(self.print_colored_text("4. Contact Information", "purple"))
            print(self.print_colored_text("5. Exit", "red"))
            print(self.print_colored_text("=" * 60, "cyan"))
            
            choice = input(self.print_colored_text("\nEnter your choice (1-5): ", "white"))
            
            if choice == "1":
                self.display_all_commands()
                input(self.print_colored_text("\nPress Enter to return to main menu...", "yellow"))
            
            elif choice == "2":
                query = input(self.print_colored_text("\nEnter command name or keyword to search: ", "white"))
                results = self.search_command(query)
                
                if results:
                    print()
                    print(self.print_colored_text(f"Found {len(results)} result(s):", "green"))
                    for num, cmd in results:
                        print(f"{self.print_colored_text(f'{num}.', 'purple')} {self.print_colored_text(cmd['name'], 'cyan')} - {cmd['desc']}")
                else:
                    print(self.print_colored_text("No commands found matching your search.", "red"))
                
                input(self.print_colored_text("\nPress Enter to continue...", "yellow"))
            
            elif choice == "3":
                try:
                    cmd_num = int(input(self.print_colored_text("\nEnter command number (1-50): ", "white")))
                    self.display_command_details(cmd_num)
                except ValueError:
                    print(self.print_colored_text("Please enter a valid number!", "red"))
                
                input(self.print_colored_text("\nPress Enter to continue...", "yellow"))
            
            elif choice == "4":
                self.display_contact_info()
                input(self.print_colored_text("\nPress Enter to continue...", "yellow"))
            
            elif choice == "5":
                print()
                self.print_typing_effect(self.print_colored_text("Thank you for using Kali Linux Commands Cheat Sheet Tool!", "green"))
                self.print_typing_effect(self.print_colored_text("Created by chowdhuryvai", "yellow"))
                print()
                break
            
            else:
                print(self.print_colored_text("Invalid choice! Please try again.", "red"))
                time.sleep(2)

if __name__ == "__main__":
    try:
        tool = KaliCommandsTool()
        tool.run()
    except KeyboardInterrupt:
        print("\n" + tool.print_colored_text("\nTool interrupted by user. Exiting...", "red"))
        sys.exit(0)

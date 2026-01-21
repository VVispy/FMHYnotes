import os
import re

notes_dir = r"c:\Users\wispy\Files\coding\fmhynotes\notes"

data = [
    {
        "title": "Malware Removal Forums",
        "content": "Note that many of these will suggest removing pirated software, but if you got everything from trusted sources, there is no real need to do that."
    },
    {
        "title": "HDO Box Note",
        "content": "To use the app, HDO Box may ask you to install a third-party video player which contains ads. Check out the DNS Adblocking section on FMHY for adblocking solutions."
    },
    {
        "title": "Buzzheavier Warning",
        "content": "Make sure you have an [adblocker](https://fmhy.net/adblockvpnguide#adblocking) when using Buzzheavier as there are hidden ads on download pages with malicious content. Both the download button and torrent buttons should automatically start a download in your browser, NOT redirect you to another page."
    },
    {
        "title": "Lutton note",
        "content": "You can ask the bot for english, but it can be hit and miss in terms of working."
    },
    {
        "title": "Spicetify Note",
        "content": "Join their [Discord](https://discord.gg/VnevqPp2Rr) for version compatibility.\n\nNote that you can use the store built in to get a full list of addons and themes."
    },
    {
        "title": "Pollinations Note",
        "content": "To use this site for image generation, scroll down to \"Image Feed\" and change it to  \"Try\" from \"Watch\". Available models are flux (schnell), turbo (SDXL Turbo), and gptimage. For gptimage, allowed resolutions are 1024x1024, 1536x1024 (landscape), and 1024x1536 (portrait). Change the seed to a random number for different output. The \"Write the 'Imagine' word only\" button is the submit button. Pretty sure its unlimited for all models, at least through UI."
    },
    {
        "title": "Pollinations Limits",
        "content": "For `chat.pollinations.ai` (and the underlying API), the rate limits depend on how you're using it:\n\n**Anonymous / Free Tier (No Login)**\n- **Text/Chat**: ~1 request every **3 seconds** (per IP).\n- **Images**: ~1 request every **5 seconds** (per IP).\n\n**Logged In (Pollen System)**\n- Users get a **daily free Pollen allowance** based on their tier.\n- **Publishable Keys (`pk_`)**: Rate limited to prevent abuse (e.g., ~1 pollen/hour per IP).\n- **Secret Keys (`sk_`)**: **No rate limits** (requests run as fast as you can pay for them with Pollen).\n\nIf you're hitting limits on the chat site:\n1. Slow down slightly (wait 3-5s between messages).\n2. **Log in** at [enter.pollinations.ai](https://enter.pollinations.ai) to use your daily free credits.\n3. If you need massive throughput, use an API key (`sk_`) with purchased credits."
    },
    {
        "title": "Mobilism Ranks",
        "content": "The users in red. Administrators are members assigned with the highest level of control over the entire board. Usually they’re Section Heads. Most Administrators are Section Heads but not all Section Heads are administrators.\n \nThe users in green. They moderate! Moderators are members of our staff who make everyone follows the site’s rules.\n \nThe users in light green. They’re similar to moderators but do not have the same authority. Oftentimes helpers eventually become moderators.\n \nThe people in orange. Mobilism has an Android Review Section and a Book Review Section. Users who are part of their review teams are the Reviewers.\n \nThe guys in purple. Different sections have different requirements for becoming a Major Releaser but generally it comes with making significant contributions to the release sections.\n \nThe users in blue. VIPs are either members who were rewarded with VIP status for their contributions, or donated to support Mobilism. VIPs have access to VIP sections: VIP Releases, VIP Requests, VIP Talk, receive extra WRZ$ and do not see any ads."
    },
    {
        "title": "CrystalDiskInfo",
        "content": "Avoid versions labeled \"Ads\"."
    },
    {
        "title": "Sora",
        "content": "Bypass the need for a invite code by installing Sora Mobile, and logging into OpenAI."
    },
    {
        "title": "Alt Warp Clients",
        "content": "If you can't connect, try Scanner Settings -> Endpoint -> Suggested -> Try different IP's to find one that works\n\n* https://github.com/bepass-org/oblivion-desktop\n* https://github.com/bepass-org/oblivion"
    },
    {
        "title": "Thunderbird",
        "content": "To get real-time notification, press the three lines in the top left corner, select the account you want to configure, select Manage Folders, then select the folder you want from below. You can then select inbox and enable push. (Notifications must be enabled)."
    },
    {
        "title": "Bookmarkeddit",
        "content": "This also extends the amount of saved posts you can view (reddit caps at 1000 by default)"
    },
    {
        "title": "Captcha 4PDA",
        "content": "Use Google Gemini to translate the captcha"
    },
    {
        "title": "Audiobookbay Warning",
        "content": "Avoid Fake download links, use [Torrents / Magnets](https://i.ibb.co/8sV2061/0fa8159b11bb.png), or paste info hash into torrent client"
    },
    {
        "title": "LiteAPK + Modyolo Note",
        "content": "The site is safe, but they are known for mislabeling things like RockMods releases as their own, and mislabeling versions to make it look like they have newer things than they really do."
    },
    {
        "title": "APKMirror Extensions",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/toolbox-google-play-store/ \n* https://chrome.google.com/webstore/detail/toolbox-for-google-play-s/fepaalfjfchbdianlgginbmpeeacahoo\n* https://addons.opera.com/en/extensions/details/toolbox-for-google-play-storetm/"
    },
    {
        "title": "TinyURL Note",
        "content": "To reveal the destination URL, replace \"www\" with \"preview\" in the URL like so:\n \nhttps://preview.tinyurl.com/5erwtst5"
    },
    {
        "title": "ChatGPT Limits",
        "content": "* GPT-5.1-medium (1 Daily)\n* GPT-5.1-chat (10 per 5 hours)\n* GPT-5.1- mini (Unlimited)"
    },
    {
        "title": "RGShows Autoplay",
        "content": "If you're using Firefox and you want autoplay, hit the permissions on your url search bar and allow both audio + video."
    },
    {
        "title": "Openasar",
        "content": "The Vencord installer has an option to install OpenAsar, but you may need to click the install button twice (only once more after clicking \"Accept\")."
    },
    {
        "title": "Eruda",
        "content": "Eruda Console for mobile browsers bookmarklet: \n \n`javascript:(function () { var script = document.createElement('script'); script.src=\"//cdn.jsdelivr.net/npm/eruda\"; document.body.appendChild(script); script.onload = function () { eruda.init() } })();`"
    },
    {
        "title": "Sport7",
        "content": "Note that many sites use this player, but Sport7 is their main site."
    },
    {
        "title": "Android Spotify Note",
        "content": "Many modded apks are buggy as of now and may not work at all."
    },
    {
        "title": "Proton Torrenting",
        "content": "Torrenting on Proton VPN's free plan is only possible when using an OpenVPN configuration / [Guide](https://protonvpn.com/support/vpn-config-download). Note that they do expire, so you'll have to make new ones occasionally.\n\nOpenVPN login credentials are located [here](https://account.protonvpn.com/account-password)."
    },
    {
        "title": "App Cake Warning",
        "content": "The site itself is safe, but in the past they've used leaked public certificates for their official app, which can get your phone(and account) blacklisted from sideloading."
    },
    {
        "title": "Bypass FREEdlink",
        "content": "You still need to bypass Cloudflare captcha by yourself. This only bypasses timer on single downloads. You may still need to wait normal time to download another file which is enforced from server-side."
    },
    {
        "title": "Video DownloadHelper",
        "content": "Note that some versions of this extension give a watermark on sites that need conversion. It seems to happen on the Windows + Firefox version."
    },
    {
        "title": "Reaper Note",
        "content": "Asks user to buy after 60 days, but you can just close the popup and keep using for free"
    },
    {
        "title": "Instaeclipse Note",
        "content": "Use ['advanced'](https://wispydocs.pages.dev/revanced-obtainium/#advanced) to build clean apks, or use antisplitm with revanced manager."
    },
    {
        "title": "Google Song Identification",
        "content": "Google and YouTube Music mobile apps have song identification button next to the search box."
    },
    {
        "title": "Google Translate Note",
        "content": "Google translate can serve as a web proxy. Simply paste your URL into the translate field and then click on the result and view the page in the original language. This way you can navigate any web-page via google.com. Google is almost never blocked so this trick works on most occasions."
    },
    {
        "title": "Aurora Note",
        "content": "Keep in mind that some apps that exist do not work unless you installed them from the google play store. This is usually true for things like banking apps, or some institutions app."
    },
    {
        "title": "App Lock",
        "content": "Keep in mind this is a privacy utility meant to prevent common snooping, its not claiming to be a security tool, and will not stop forensic analysis."
    },
    {
        "title": "Flicker Proxy",
        "content": "Note that the proxy may be slower, but it can be used in cases where the site or TMDb is blocked."
    },
    {
        "title": "Site Favicon DL",
        "content": "You can also do `https://www.google.com/s2/favicons?domain=URL&sz=64` where URL is the URL of the site you want and sz is the size in pixels"
    },
    {
        "title": "Foxit Warning",
        "content": "The installer tries to install McAfee WebAdvisor + PhantomPDF Business. They can be skipped by clicking \"decline\" both times."
    },
    {
        "title": "Yet Another Call Blocker Note",
        "content": "The app itself isn't maintained, but the repo contains the \"main\" phone number database. It is updated once in a couple of months. The app receives daily (incremental) updates directly from third-party services."
    },
    {
        "title": "Sanet Warning",
        "content": "Note that Sanet has been known to host things like KMS Matrix, so its best to avoid it for software and games"
    },
    {
        "title": "Advanced Logic Calculators",
        "content": "* analytic tableaux generator: https://www.umsu.de/trees/\n* natural deduction proof checker: https://proofs.openlogicproject.org/\n* propositional logic calculator (finds models): https://www.inf.unibz.it/~franconi/teaching/propcalc/\n* a tutorial on sequent calculus: http://logitext.mit.edu/tutorial\n* modal logic playground (for constructing models): https://rkirsling.github.io/modallogic/"
    },
    {
        "title": "SD Maid",
        "content": "Google play version is paid. Press donate to unlock the app on F-Droid and GitHub versions."
    },
    {
        "title": "Glitchwave Note",
        "content": "For charts you can specify months and days using URLs like the following examples\n\nJanuary 2006:\n`https://glitchwave.com/charts/popular/game/2006.01/excl:ratings/`\n\nJan-Feb 2018:\n`https://glitchwave.com/charts/popular/game/2018.01-2018.02/excl:ratings/`"
    },
    {
        "title": "Filebin Warning",
        "content": "Anyone with a link to a \"bin\" has full access to it. They can add new files, delete existing files, etc"
    },
    {
        "title": "Fluxy Repacks",
        "content": "Note that though it has repacks in the name, its not actually a repack site."
    },
    {
        "title": "Filelu Warning",
        "content": "According to their FAQ question \"When will my files expire?\", you must login to your account at least once every 180 days to prevent your account being deleted."
    },
    {
        "title": "SoftArchive Mirrors",
        "content": "- https://sanet.download/\n- https://softarchive.is/\n- https://sanet.lc/\n- https://sanet.ws/\n- https://sanet.st/\n- https://sanet.sb/\n- https://soft.ac/"
    },
    {
        "title": "Soft98 Note",
        "content": "Enable `AdGuard - Ads` filterlist in uBlock to allow downloads to work. To remove all ads, you can also get the [AdGuard Extra Userscript](https://github.com/AdguardTeam/AdGuardExtra?tab=readme-ov-file#userscript) (not the extension) and enable it in your script manager. Note that you may need to disable filter `ir: PersianBlocker`."
    },
    {
        "title": "OneClick Note",
        "content": "Main features include:\n- Download links straight to Google Drive.\n- Torrent to Google Drive.\n- Google Drive Download Manager (similar to pyLoad).\n- Spotify Downloader.\n- Jellyfin Support.\n- RClone + WebUI.\n- And much more."
    },
    {
        "title": "MovieParadise Code",
        "content": "* In order to unlock the better host (1fichier) you need to signup code. This is important as without it the site will be rapidgator only links which are very slow. You can get a code from the link below, or the pins in our #free-stuff discord channel.\n\n**[Click Here To Get Code](https://rentry.org/he8fhzku)**"
    },
    {
        "title": "Megabasterd Note",
        "content": "Free proxies work but they are very hit and miss"
    },
    {
        "title": "SH Note",
        "content": "Based on popular [card game](https://en.wikipedia.org/wiki/Secret_Hitler), created by cards against humanity co-founder."
    },
    {
        "title": "Māori Note",
        "content": "Māori is the indigenous language of mainland New Zealand. Due to the [Native Schools Act](https://en.wikipedia.org/wiki/M%C4%81ori_language#Suppression_and_decline) in 1867, children were forbidden to speak it in the classroom, under penalty of corporal punishment, which led to a rapid decline of speakers. There are now [revitalization efforts](https://en.wikipedia.org/wiki/M%C4%81ori_language_revival) (such as Tōku Reo) attempting to promote and reinforce its use."
    },
    {
        "title": "Steam Currency Converter Note",
        "content": "For instant currency conversion : Go to Firefox's extensions settings, click on the add-on, enter the permissions section and allow the sites there"
    },
    {
        "title": "Vuenxx Note",
        "content": "If you want to download the files, you need to send the screenshot that you subscribed to the vuenxx youtube channel to the discord \"teyit\" channel. After a while the download channels will open."
    },
    {
        "title": "Steam Controller Support",
        "content": "Steam has built in support for most controller types, just add your games to steam, right click the game, and turn on your controller"
    },
    {
        "title": "WinRAR",
        "content": "WinRAR does not auto-update, and because it had a remote code execution vulnerability in the past, you should make sure you've manually updated **to 7.13 or later** to be safe."
    },
    {
        "title": "IRC Highway Note",
        "content": "To request a book run: @request [author] [title] - Requests without both [author] and [title] are deleted.\n \nTo view request status and rules run: @request-list"
    },
    {
        "title": "DODI Warning",
        "content": "Its highly recommended to stick to dodi's 1337x page or main website, as sites they linked to have fake DDL buttons, and shouldn't be used without an adblocker"
    },
    {
        "title": "Ranks 1337x",
        "content": "* :black_large_square:  Black - Admin\n* :green_square: Green - Moderator\n* :blue_square:  Blue - VIP (Very Trusted)\n* :yellow_square: Yellow - Uploader (Trusted)\n* :red_square:  Red - Trial Uploader\n* :white_large_square:  Grey - User"
    },
    {
        "title": "FreeGOGPCGames Note",
        "content": "Many titles on the site are the older versions of the installers. The digital signature on the installer is signed by GOG Limited, which is the old company name before it was merged with GOG Sp. z o.o and all digital file signatures were updated to reflect this name change.\n \nThe hash does not match the gog-games database because the digital file signatures differ on the installer. Installing either version will produce identical sets of files since the game version remains unchanged.\n \n/u/AtariRiot66"
    },
    {
        "title": "movie-web",
        "content": "You can [enable an extension](https://pstream.org/onboarding/extension) / [2](https://github.com/sussy-code/browser-ext/releases/) that will add more sources, but it needs to connect to all sites to function. The extension is safe, and many people use it, the permissions are just needed in order for the [extension to work correctly](https://rentry.co/htagcrv4). \n\nNote that it can be ran in a new browser or fresh browser profile if you don't want to use your main browser.\n\nFor a setup guide (including 4k) you can watch this video: \nhttps://vimeo.com/1059834885/c3ab398d42\n\nDocs + selfhosting guides can be found here: \nhttps://docs.pstream.mov/"
    },
    {
        "title": "Eaglercraft Note",
        "content": "Play on Chromium-based browsers for the best performance"
    },
    {
        "title": "TeamSpeak Warning",
        "content": "Note that teamspeak server admins can view IPs, so only join servers you trust"
    },
    {
        "title": "WeLib Note",
        "content": "WeLib is *not* connected to Anna's Archive, they simply mirror Anna's content onto their own site that has a different UI. It is not updated as often, and they don't share their codebase improvements publicly, so they aren't endorsed by Anna's themselves."
    },
    {
        "title": "General Tweak Warning",
        "content": "Its not recommended to use these unless you know what you're doing. Always research first, never just \"Apply All\" tweaks randomly."
    },
    {
        "title": "ScrollAnywhere Addons",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/scroll_anywhere/\n* https://chrome.google.com/webstore/detail/scrollanywhere/jehmdpemhgfgjblpkilmeoafmkhbckhi\n* https://addons.opera.com/en/extensions/details/scrollanywhere/?display=en"
    },
    {
        "title": "Clipboard2File Addons",
        "content": "* https://github.com/vord1080/clipboard2file/\n* https://github.com/daijro/Clipboard2File-Chrome"
    },
    {
        "title": "YouTube Tweaks",
        "content": "* https://addons.mozilla.org/firefox/addon/youtube-tweaks/\n* https://chrome.google.com/webstore/detail/youtube-tweaks/oeakphpfoaeggagmgphfejmfjbhjfhhh"
    },
    {
        "title": "PrintEditWe Addons",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/print-edit-we/\n* https://chrome.google.com/webstore/detail/print-edit-we/olnblpmehglpcallpnbgmikjblmkopia"
    },
    {
        "title": "SavePageWe",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/save-page-we/\n* https://chrome.google.com/webstore/detail/save-page-we/dhhpefjklgkmgeafimnjhojgjamoafof"
    },
    {
        "title": "Better Reasoning",
        "content": "For better reasoning, switch mode to \"think deeper\""
    },
    {
        "title": "Cofi Note",
        "content": "Useful if you're a coffee enthusiast. The methods are created by James Hoffmann, he's a world champion barista and popular YouTuber"
    },
    {
        "title": "Tautulli Note",
        "content": "This will sometimes get falsely flagged by defender and removed automatically, so it may need to be allowed manually."
    },
    {
        "title": "CS.RIN Search",
        "content": "If your initial search doesn't work, trying searching the same term again within the \"search these results\" engine on the results screen. \n\n<img width=\"1307\" height=\"97\" alt=\"image\" src=\"https://github.com/user-attachments/assets/b2f149b9-8a9a-4250-8754-e63f50b82c59\" />"
    },
    {
        "title": "Forest Extensions",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/forest-stay-focused-be-present/\n* https://chrome.google.com/webstore/detail/forest-stay-focused-be-pr/kjacjjdnoddnpbbcjilcajfhhbdhkpgk"
    },
    {
        "title": "Jdownloader",
        "content": "Keep in mind the link on their frontpage is sponsored and has adware, but jdownloader2 which is linked on fmhy, does not contain any adware."
    },
    {
        "title": "FileZilla",
        "content": "Keep in mind the link on their frontpage is sponsored and has adware, but you can get to the non-adware version by following the link on fmhy, \nor pressing download on the FileZilla website, and then clicking \"additional downloads\" under the big download button."
    },
    {
        "title": "Edith Login",
        "content": "`user: edith` \n`pw: jarvis`"
    },
    {
        "title": "Alt Twitch Player Extensions",
        "content": "* https://addons.mozilla.org/en-US/firefox/addon/twitch_5/\n* https://chrome.google.com/webstore/detail/alternate-player-for-twit/bhplkbgoehhhddaoolmakpocnenplmhf"
    },
    {
        "title": "Tabiverse Extensions",
        "content": "* https://addons.mozilla.org/firefox/addon/tabiverse/\n* https://chromewebstore.google.com/detail/hpplgjkooibhfkmmepoikcjpadcojcik"
    },
    {
        "title": "MVSEP Note",
        "content": "Register for wav and flac output, and lower queue times"
    },
    {
        "title": "Driver Note",
        "content": "Only install the drivers you actually need. Don't install all new drivers at once, as this could lead to things breaking, especially system audio."
    },
    {
        "title": "Buster Note",
        "content": "The client app simulates user interactions which greatly improves the success rate of buster. You can download the app through the extensions option page, or get it from the link below: \n\nhttps://github.com/dessant/buster-client\n\nThe app is available for Windows, Linux, and macOS"
    },
    {
        "title": "Dolby Access / Atmos Note",
        "content": "Many headsets come with Dolby Access for free without letting users know. You can check if you're licensed by opening Dolby Access, going to settings, and looking in the [bottom right corner](https://i.imgur.com/9vJA6CL.png). Its much better than things like iCue or similar apps."
    },
    {
        "title": "RedditFilter Note",
        "content": "Go to Settings → Feed Filter and untoggle 'Promoted' to not see ads. Those that don't like AI suggestions can untoggle 'Recommended' as well."
    },
    {
        "title": "OpenRGB Beta",
        "content": "How to download OpenRGB beta.\n \nWhy?\n  Because the latest version that you can download from the website dates from July 9 2023, and since a new device is added to the software almost every day, using the beta version becomes a necessity.\n \nGo to Gitlab OpenRgb site `https://gitlab.com/CalcProgrammer1/OpenRGB` and on the left go to Build => Pipelines and then download the appropriate version from the download button on the top right.\n(Note: Before downloading it should say Passed at the top left.)\n \nSupported devices (0.9) => `https://openrgb.org/devices_0.9.html`\n(The link may become outdated after a while, go to the OpenRGB site `https://openrgb.org/index.html` and find the newer one in the menu on the top right.)\n \nSupported devices (Latest experimental) => `https://openrgb.org/devices.html`"
    },
    {
        "title": "YTS / Yify Note",
        "content": "YTS / Yify has many fake ripoff sites out there, make 100% sure you're on one of the official domains before downloading."
    },
    {
        "title": "Limit Bypass Note",
        "content": "- sparsebox: ios 17.0 - 18.1 beta 4 (not including 17.7.1, 17.7.2)\n- live container: ios 16+"
    },
    {
        "title": "m0nkrus",
        "content": "![image](https://github.com/user-attachments/assets/3d463300-098d-4392-8710-84dcb7b47a03)"
    }
]

if not os.path.exists(notes_dir):
    os.makedirs(notes_dir)

for item in data:
    title = item["title"]
    content = item["content"]
    
    # Generate filename
    slug = title.lower().replace("+", "plus").replace("/", "-")
    # Remove characters that aren't allowed in filenames or might be annoying
    slug = re.sub(r'[^a-z0-9\- ]', '', slug)
    slug = slug.strip().replace(" ", "-")
    filename = slug + ".md"
    
    file_path = os.path.join(notes_dir, filename)
    
    file_content = f"# {title}\n\n{content}\n"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
    
    print(f"Created: {filename}")

print("Done.")

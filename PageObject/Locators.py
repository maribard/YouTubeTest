class Locator(object):
    search_box = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form'
    search_icon = '//*[@id="search-icon-legacy"]'
    search_input = 'search'
    ytd_list_video = '//*[@id="content"]/a'
    accept_cookie = "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]" \
                    "/ytd-button-renderer[2]/yt-button-shape/button"
    result_of_search = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/' \
                       'div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]'
    play_button = '//*[@id="movie_player"]/div[33]/div[2]/div[1]/button'
    skip_add = '//*[@class="ytp-ad-skip-button-slot"]/span/button'
    spec_button = '//*[@id="dismiss-button"]/yt-button-shape/button'
    mute_video = '//button[@class="ytp-mute-button ytp-button"]'
    video_box = '//*[@id="movie_player"]/div[1]/video'
    login_button = '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'
    current_time = '//*[@id="movie_player"]/div[33]/div[2]/div[1]/div[1]/span[2]/span[1]'
    expand_container = '//*[@id="expand" and @class="button style-scope ytd-text-inline-expander"]'
    amount_of_likes = '//*[@id="segmented-like-button"]/ytd-toggle-button-renderer/yt-button-shape/button/div[2]/span'
    date_of_upload = '//*[@id="info"]/span[3]'
    amount_of_views = '//*[@id="info"]/span[1]'
    next_video_button = '//*[@class="ytp-next-button ytp-button"]'
    channel_name = '//div[contains(@class, "channel-name")]//a'
    duratiorn_video = '//*[@class="ytp-time-duration"]'
    title_video = '//*[@id="title"]/h1'
    slide_bar = '//*[@id="movie_player"]/div[33]/div[1]/div[2]'
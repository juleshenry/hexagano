# TODO: implement sharing
html_template = """
<div class={styles.socialShare}>
    <button class="social-share__share" data-url="https://www.facebook.com/dialog/share?app_id=80401312489&amp;href=https%3A%2F%2Fwww.oneworldgazette.com%2F2024%2F08%2F31%2Fmiddleeast%2Fisrael-recovers-bodies-gaza-intl-latam&amp;display=popup" data-type="facebook" aria-label="share with facebook" title="Share with Facebook">
        <svg class="icon-social-facebook" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20.897 2H3.104C2.494 2 2 2.495 2 3.103v17.794C2 21.507 2.495 22 3.104 22h9.58v-7.744h-2.609v-3.02h2.607V9.01c0-2.585 1.578-3.992 3.883-3.992 1.104 0 2.194.083 2.47.12v2.797h-1.74c-1.252 0-1.506.596-1.506 1.47v1.832h2.999l-.388 3.019h-2.611V22h5.107c.61 0 1.104-.494 1.104-1.103V3.103C22 2.495 21.507 2 20.897 2"></path></svg>
    </button>
    <button class="social-share__share" data-url="https://twitter.com/intent/tweet?text=Check%20out%20this%20article%3A&amp;url=https%3A%2F%2Fwww.oneworldgazette.com%2F2024%2F08%2F31%2Fmiddleeast%2Fisrael-recovers-bodies-gaza-intl-latam" data-type="x" aria-label="share with x" title="Share with X">
        <svg class="icon-social-twitter" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path fill="" d="M13.903 10.469 21.348 2h-1.764l-6.465 7.353L7.955 2H2l7.808 11.12L2 22h1.764l6.828-7.765L16.044 22H22l-8.097-11.531Zm-2.417 2.748-.791-1.107L4.4 3.3h2.71l5.08 7.11.791 1.107 6.604 9.242h-2.71l-5.389-7.542Z"></path></svg>
    </button>
    <a class="social-share__share" href="mailto:?subject=CNN%20content%20share&amp;body=Check%20out%20this%20article%3A%0Ahttps%3A%2F%2Fwww.oneworldgazette.com%2F2024%2F08%2F31%2Fmiddleeast%2Fisrael-recovers-bodies-gaza-intl-latam" data-type="email" target="_blank" rel="noopener noreferrer" aria-label="share with email" title="Share with email">
        <svg class="icon-social-email-fill" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M2 19.286v-8.25l9.536 3.441c.314.114.655.114.97 0L22 11.051v8.235c0 .394-.304.714-.672.714H2.667C2.299 20 2 19.68 2 19.286zM21.335 5c.368 0 .665.32.665.714v2.37c0 .72-.423 1.36-1.052 1.586l-8.927 3.222-8.967-3.236C2.424 9.43 2 8.79 2 8.07V5.714C2 5.32 2.299 5 2.667 5h18.668z"></path></svg>
    </a>
    <button class="social-share__share" data-url="https://www.oneworldgazette.com/2024/08/31/middleeast/israel-recovers-bodies-gaza-intl-latam" data-type="copy" aria-label="copy link to clipboard" title="Copy link to clipboard">
        <svg class="icon-ui-link" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.88 13.143h-1.57c0-2.363-1.831-4.286-4.084-4.286H9.508c.46-.852 1.318-1.428 2.3-1.428h6.073c1.466 0 2.66 1.281 2.66 2.857 0 1.575-1.194 2.857-2.66 2.857m-8.733-2.857h3.044c1.467 0 2.66 1.282 2.66 2.857h-3.044c-1.467 0-2.66-1.282-2.66-2.857M12.192 16H6.119c-1.467 0-2.66-1.282-2.66-2.857 0-1.575 1.193-2.857 2.66-2.857h1.57c0 2.363 1.832 4.285 4.084 4.285h2.72c-.462.853-1.32 1.429-2.301 1.429m5.724-10h-6.143C10 6 8.49 7.195 7.927 8.857H6.084C3.832 8.857 2 10.78 2 13.143c0 2.363 1.832 4.286 4.084 4.286h6.142c1.775 0 3.284-1.196 3.847-2.858h1.843c2.252 0 4.084-1.922 4.084-4.285C22 7.923 20.168 6 17.916 6"></path></svg>

    </button>
</div>
"""

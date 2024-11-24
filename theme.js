
    function switchTheme() {
        const currentTheme = document.getElementById('theme-style').getAttribute('href');
        const newTheme = currentTheme === 'light.css' ? 'dark.css' : 'light.css';
        document.getElementById('theme-style').setAttribute('href', newTheme);
    }
    
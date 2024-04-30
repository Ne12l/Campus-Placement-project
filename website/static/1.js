document.addEventListener('DOMContentLoaded', function() {
    var profileWindow = document.getElementById('profile-window');
    var toggleProfileButton = document.getElementById('toggle-profile');
    var closeButton = document.getElementById('close-button');

    toggleProfileButton.addEventListener('click', function() {
        profileWindow.style.right = '0';
    });

    closeButton.addEventListener('click', function() {
        profileWindow.style.right = '-250px';
    });
});

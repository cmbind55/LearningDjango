var initialize = function (navigator, user, token, urls) {
    console.log("navigator initialize: " + navigator);
    $('#id_login').on('click', function () {
        navigator.id.request();
    });
    $('#id_logout').on('click', function () {
        navigator.id.logout();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            var deferred = $.post(
                urls.login,
                { assertion: assertion, csrfmiddlewaretoken: token }
            );
            deferred.done(function () { window.location.reload(); })
            deferred.fail(function () { navigator.id.logout(); });
        },
        onlogout: function (){
            console.log("logging out...");
            navigator.id.logout();
        }
    });
};

window.lists = {
    Accounts: {
        initialize: initialize
    }
};

P = {
    Addition: {}
};

P.Addition.check = function() {
    var f = document.forms["addition"];
    var lastelapsed = <?php echo $lastelapsed; ?>;
    var numbers = <?php echo $numbers; ?>;
    var digits = <?php echo $digits; ?>;
    var all = true;
    for (var i = 0; i < f.elements["sumattempt"].length; i++) {
        if (f.elements["sumattempt"][i].value != f.elements["sum"][i].value) {
            f.elements["sumattempt"][i].value = "";
            all = false;
        }
    }
    if (all) {
        endtime = new Date();
        startseconds = starttime.getMinutes() * 60 + starttime.getSeconds();
        endseconds = endtime.getMinutes() * 60 + endtime.getSeconds();
        secondselapsed = endseconds - startseconds;
        if (secondselapsed < lastelapsed) {
            if (numbers < 8) {
                f.numbers.value = numbers + 1;
            }
            else {
                f.numbers.value = 3;
                f.digits.value = digits + 1;
            }
        }
        f.lastelapsed.value = secondselapsed;

        alert("Excellent:  you added each column correctly.  It took you " + secondselapsed + " seconds.");
        f.submit();
    }
    
}

P.Addition.starttime = new Date();

P.Addition.initFocus = function() {
    var f = document.forms["addition"];
    f.elements["sumattempt"][0].focus();
}

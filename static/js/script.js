// Add an event listener to the combined input area
document.getElementById('teamSearch').addEventListener('input', function () {
    var input, filter, select, option, i;
    input = document.getElementById('teamSearch');
    filter = input.value.toUpperCase();
    select = document.getElementById('team_id');
    option = select.getElementsByTagName('option');

    // Loop through all options in the select element
    for (i = 0; i < option.length; i++) {
        // If the team name contains the input value, display the option, otherwise hide it
        if (option[i].textContent.toUpperCase().indexOf(filter) > -1) {
            option[i].style.display = '';
        } else {
            option[i].style.display = 'none';
        }
    }
});

document.getElementById('playerSearch').addEventListener('input', function () {
    var input, filter, select, option, i;
    input = document.getElementById('playerSearch');
    filter = input.value.toUpperCase();
    select = document.getElementById('playerID');
    option = select.getElementsByTagName('option');

    // Loop through all options in the select element
    for (i = 0; i < option.length; i++) {
        // If the team name contains the input value, display the option, otherwise hide it
        if (option[i].textContent.toUpperCase().indexOf(filter) > -1) {
            option[i].style.display = '';
        } else {
            option[i].style.display = 'none';
        }
    }
} );

// tooltip for hovering the admin buttons
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
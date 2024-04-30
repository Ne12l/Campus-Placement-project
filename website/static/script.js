$(document).ready(function(){
      $('.menu-icon').click(function(){
        $('.menu-icon').toggleClass('active')
      })
    })

//client//
    $(function() {
      var $clientslider = $('#clientlogo');
      var clients = $clientslider.children().length;
      var clientwidth = (clients * 220); 
      $clientslider.css('width', clientwidth);
      var rotating = true;
      var clientspeed = 1800;
      var seeclients = setInterval(rotateClients, clientspeed);
      $(document).on({
        mouseenter: function() {
          rotating = false;
        },
        mouseleave: function() {
          rotating = true;
        }
      }, '#ourclients');
      function rotateClients() {
        if (rotating != false) {
          var $first = $('#clientlogo li:first');
          $first.animate({
            'margin-left': '-220px'
          }, 2000, function() {
            $first.remove().css({
              'margin-left': '0px'
            });
            $('#clientlogo li:last').after($first);
          });
        }
      }
    });
    //placement hub
    $("#searchInput").focus(function () {
  
      $("#searchInput").css({
        "display": "inline",
        "width": "40%",
        "border": "1px solid #40585d",
        "opacity": "1",
        "padding": "8px 20px 8px 20px",
        "background-image": "none",
        "box-shadow": "0 0 1px black"
      });
      $("#submitsearch").css("display", "inline");
     
      $("#searchInput").prop("placeholder", "");
    });

    //login page//
    const inputs = document.querySelectorAll("input");
inputs.forEach(function (input) {
  input.addEventListener("focus", function () {
    const parentElement = input.parentElement.parentElement;
    parentElement.classList.add("box-animation");
  });
  input.addEventListener("blur", function () {
    const parentElement = input.parentElement.parentElement;
    parentElement.classList.remove("box-animation");
  });
});

const buttons = document.querySelectorAll("#multiple-btn button");
const form_container = document.getElementById('form_section')
buttons.forEach((button) => {
button.addEventListener("click", () => {
form_container.classList.toggle("left-right");

});
});

//profile//

document.addEventListener('DOMContentLoaded', function() {
  var profileLink = document.getElementById('profile-link');
  var profileWrapper = document.getElementById('profile-wrapper');
  var profileWindow = document.getElementById('profile-window');
  var closeButton = document.getElementById('close-button');

  profileLink.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent the default link behavior
      profileWrapper.classList.toggle('show-profile');
  });

  closeButton.addEventListener('click', function() {
      profileWrapper.classList.remove('show-profile');
  });
});

// Dummy job data
let jobs = [];

// Function to display jobs
function displayJobs() {
    const jobList = document.getElementById('jobList');
    jobList.innerHTML = '';

    jobs.forEach((job, index) => {
        const jobItem = document.createElement('div');
        jobItem.classList.add('job-item');
        jobItem.innerHTML = `
            <h3>${job.title}</h3>
            <p>${job.description}</p>
            <button onclick="applyForJob(${index})">Apply</button>
        `;
        jobList.appendChild(jobItem);
    });
}

// Function to post a job
document.getElementById('jobForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const jobTitle = document.getElementById('title').value;
    const jobDescription = document.getElementById('description').value;

    if (jobTitle && jobDescription) {
        const job = {
            title: title,
            description: description,
            applicants: []
        };
        jobs.push(job);
        displayJobs();
        document.getElementById('jobForm').reset();
    } else {
        alert('Please fill out all fields.');
    }
});

// Function to apply for a job
function applyForJob(jobIndex) {
    const fullName = prompt('Enter your full name:');
    if (fullName) {
        const job = jobs[jobIndex];
        job.applicants.push(fullName);
        alert('You have successfully applied for the job.');
        displayJobs();
    }
}

// Initial display of jobs
displayJobs();


/* ----- Accordion ----- */
$(document).ready(function () {
    var url = (window.location).href;
    var id = url.substring(url.lastIndexOf('#') + 1);
    if (id != url) {
        $(".accordion h2").removeClass('current');
        $('#' + id).addClass("current");
        $('#' + id).next(".pane").slideDown('slow');
    } else {
      
      $(".pane").slideDown("slow");
      
    }
  
    $(".accordion h2").click(function () {
        $(this).next(".pane").slideToggle("slow").siblings(".pane:visible").slideUp("slow");
        $(this).toggleClass("current").siblings("h2").removeClass("current");
        var link = $(this).find('a').attr("href");
        if (link == "javasrcipt:void(0);") {
            return false;
        }
    });
});    

        $(document).ready(function () {
            var showChar = 250;
            var ellipsestext = "...";
            var moretext = "Read More";
            var lesstext = "Show Less";
            $('.testi-text').each(function () {
                var content = $(this).html();
                if (content.length > showChar) {
                    var c = content.substr(0, showChar);
                    var h = content.substr(showChar, content.length - showChar);
                    var html = c + '<span class="moreellipses">' + ellipsestext + '&nbsp;<\/span><span class="morecontent"><span>' + h + '<\/span>&nbsp;&nbsp;<a href="" class="morelink" aria-label="Know more about Testimonial">' + moretext + '<\/a><\/span>';
                    $(this).html(html);
                }
            });
            $(".morelink").click(function () {
                if ($(this).hasClass("less")) {
                    $(this).removeClass("less");
                    $(this).html(moretext);
                }
                else {
                    $(this).addClass("less");
                    $(this).html(lesstext);
                }
                $(this).parent().prev().toggle();
                $(this).prev().toggle();
                return false;
            });
        });
   

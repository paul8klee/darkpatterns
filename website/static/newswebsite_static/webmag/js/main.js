// --- Begin of customization for study purposes --- //

$(document).ready(function () {
  // open modal once document is loaded
  $('#myModal').modal('show')
})
// prevent modal from closing if you click outside of it or use Esc
$('#myModal').modal({ backdrop: 'static', keyboard: false })


// require input before continuation possible
$(function () {
  $('#myForm').validate({
    rules: {
      consentForm: 'required'
    },
    messages: {
      consentForm: {
        required: 'Please select one of the options'
      }
    },
    errorElement: 'div',
    errorLabelContainer: '.errorTxt'
  })
});

$("input[type='radio']").change(function() {
  if($(this).val()=='DNA')
  {
    document.getElementById('errorTxt2').innerHTML = ''
  }
})

function directCorrect() {
  // if the form returns 'manage options' go to page 2 otherwise submit form
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'MO') {
    sendEvent(2)
  }
  // if the form returns 'Agree' submit form
  else {
    $('#myForm').submit();
  }
};

function submitCorrect() {
  var radio_value = $('input[name=consentForm]:checked').val();
  if (radio_value === 'DNA') {
    $('#myForm').submit();
  }
  else {
    document.getElementById('errorTxt2').innerHTML = 'Please select one of the options'
  }
}

// ---- End of customization for study purposes --- //

(function($) {
	"use strict"

	// Fixed Nav
	var lastScrollTop = 0;
	$(window).on('scroll', function() {
		var wScroll = $(this).scrollTop();
		if ( wScroll > $('#nav').height() ) {
			if ( wScroll < lastScrollTop ) {
				$('#nav-fixed').removeClass('slide-up').addClass('slide-down');
			} else {
				$('#nav-fixed').removeClass('slide-down').addClass('slide-up');
			}
		}
		lastScrollTop = wScroll
	});

	// Search Nav
	$('.search-btn').on('click', function () {
		$('.search-form').addClass('active');
	});

	$('.search-close').on('click', function () {
		$('.search-form').removeClass('active');
	});

	// Aside Nav
	$(document).click(function(event) {
		if (!$(event.target).closest($('#nav-aside')).length) {
			if ( $('#nav-aside').hasClass('active') ) {
				$('#nav-aside').removeClass('active');
				$('#nav').removeClass('shadow-active');
			} else {
				if ($(event.target).closest('.aside-btn').length) {
					$('#nav-aside').addClass('active');
					$('#nav').addClass('shadow-active');
				}
			}
		}
	});

	$('.nav-aside-close').on('click', function () {
		$('#nav-aside').removeClass('active');
		$('#nav').removeClass('shadow-active');
	});

	// Sticky Shares
	var $shares = $('.sticky-container .sticky-shares'),
	$sharesHeight = $shares.height(),
	$sharesTop,
	$sharesCon = $('.sticky-container'),
	$sharesConTop,
	$sharesConleft,
	$sharesConHeight,
	$sharesConBottom,
	$offsetTop = 80;

	function setStickyPos () {
		if ($shares.length > 0) {
			$sharesTop = $shares.offset().top
			$sharesConTop = $sharesCon.offset().top;
			$sharesConleft = $sharesCon.offset().left;
			$sharesConHeight = $sharesCon.height();
			$sharesConBottom = $sharesConHeight + $sharesConTop;
		}
	}

	function stickyShares (wScroll) {
		if ($shares.length > 0) {
			if ( $sharesConBottom - $sharesHeight - $offsetTop < wScroll ) {
				$shares.css({ position: 'absolute', top: $sharesConHeight - $sharesHeight , left:0});
			} else if ( $sharesTop < wScroll + $offsetTop ) {
				$shares.css({ position: 'fixed', top: $offsetTop, left: $sharesConleft });
			} else {
				$shares.css({position: 'absolute', top: 0, left: 0});
			}
		}
	}

	$(window).on('scroll', function() {
		stickyShares($(this).scrollTop());
	});

	$(window).resize(function() {
		setStickyPos();
		stickyShares($(this).scrollTop());
	});

	setStickyPos();

})(jQuery);

$('a').bind("click.myDisable", function() {
    return false;
});

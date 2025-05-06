$('.tabs button').click(function () {
  const container = $(this).closest('.stream-box');
  container.find('.tab-btn').removeClass('active');
  $(this).addClass('active');
  container.find('.resource-table').hide();
  container.find($(this).data('target')).fadeIn();
});
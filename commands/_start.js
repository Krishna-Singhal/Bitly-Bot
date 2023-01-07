/*CMD
  command: /start
  help: 
  need_reply: false
  auto_retry_time: 
  folder: 

  <<ANSWER
Welcome to link shortner bot.

Send Any Link I Will Short It
  ANSWER

  <<KEYBOARD

  KEYBOARD
  aliases: 
CMD*/

var startMessage = `Hello

I am Bitly Bot to shorten links.
Send Any Link I Will Short It.

<b>Developed by: @Sarvottama</b>`;
Api.sendMessage({
  text: startMessage,
  parse_mode: "HTML"
});

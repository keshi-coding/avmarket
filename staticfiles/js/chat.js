// Objeto para armazenar WebSockets ativos
if (typeof window.chatSockets === "undefined") {
  window.chatSockets = {};
}

// Capturar user1 corretamente ao carregar a página
document.addEventListener("DOMContentLoaded", function () {
  const user1Element = document.getElementById("logged-user");
  if (!user1Element) {
    console.error("❌ Erro: Elemento com ID 'logged-user' não encontrado!");
    return;
  }

  window.user1 = user1Element.dataset.username;

  if (!window.user1) {
    console.error("❌ Erro: user1 não foi definido corretamente!");
    return;
  }

  console.log(`✅ Usuário logado identificado como: ${window.user1}`);

  let chatList = document.getElementById("chat-list");
  if (!chatList) {
    console.error("❌ Erro: Lista de contatos (chat-list) não encontrada.");
    return;
  }

  chatList.querySelectorAll("p").forEach((userElement) => {
    userElement.addEventListener("click", function () {
      let user2 = this.dataset.username || this.textContent.trim();
      if (!window.user1 || !user2) {
        console.error(
          "❌ Erro: user1 ou user2 não definido ao clicar no contato."
        );
        return;
      }

      console.log(`🔄 Abrindo chat entre ${window.user1} e ${user2}...`);

      abrirJanelaChat(window.user1, user2);
      conectarWebSocket(window.user1, user2);
    });
  });

  let messengerIcon = document.getElementById("messenger-icon");
  let closeButton = document.getElementById("close-messenger");
  let sidebar = document.getElementById("messenger-sidebar");

  if (messengerIcon && closeButton && sidebar) {
    messengerIcon.addEventListener("click", function () {
      sidebar.style.right = "0";
      sidebar.style.display = "block";
    });

    closeButton.addEventListener("click", function () {
      sidebar.style.right = "-320px";
      setTimeout(() => {
        sidebar.style.display = "none";
      }, 300);
    });
  } else {
    console.error("❌ Erro: Algum elemento do Messenger não foi encontrado.");
  }
});

function organizarJanelasChat() {
  let chatWindows = document.querySelectorAll(".chat-window");
  let totalJanelas = chatWindows.length;
  let espacamento = 310; // Largura da janela + margem
  let direitaInicial = 20;

  chatWindows.forEach((chat, index) => {
    chat.style.right = `${direitaInicial + index * espacamento}px`;
    chat.style.bottom = "0px";
    chat.style.position = "fixed";
  });
}

// Função para abrir uma janela de chat dinamicamente
function abrirJanelaChat(user1, user2) {
  if (!user1 || !user2) {
    console.error("❌ Erro: user1 ou user2 não está definido ao abrir o chat!");
    return;
  }

  console.log(`📌 Criando janela de chat entre ${user1} e ${user2}...`);

  let existente = document.querySelector(
    `.chat-window[data-username="${user2}"]`
  );
  if (existente) return;

  let chatBox = document.createElement("div");
  chatBox.classList.add("chat-window");
  chatBox.dataset.username = user2;
  chatBox.innerHTML = `
        <div class="chat-header">
            <span>${user2}</span>
            <button class="minimize-chat">−</button>
            <button class="close-chat">×</button>
        </div>
        <div class="chat-body">
            <div class="chat-log" id="chat-log-${user2}-${user1}"></div>
        </div>
        <div class="chat-footer">
            <textarea class="chat-input"></textarea>
            <button class="send-message">Enviar</button>
        </div>
    `;

  document.body.appendChild(chatBox);
  organizarJanelasChat();

  chatBox.querySelector(".close-chat").addEventListener("click", function () {
    chatBox.remove();
  });

  chatBox.querySelector(".send-message").addEventListener("click", function () {
    let messageInput = chatBox.querySelector(".chat-input");
    let message = messageInput.value.trim();
    if (message !== "") {
      sendMessage(user1, user2, message);
      messageInput.value = "";
    }
  });
}

// Função para conectar ao WebSocket
function conectarWebSocket(user1, user2) {
  if (!user1 || !user2) {
    console.error(
      "❌ Erro: user1 ou user2 não está definido ao conectar WebSocket!"
    );
    return;
  }

  console.log(`🔄 Tentando conectar WebSocket para ${user1} e ${user2}...`);

  if (window.chatSockets[user2]) {
    console.log(`✅ WebSocket já conectado para ${user1} e ${user2}.`);
    return;
  }

  const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat/${user1}/${user2}/`
  );

  chatSocket.onopen = function () {
    console.log(`✅ WebSocket conectado para ${user1} e ${user2}`);
    window.chatSockets[user2] = chatSocket;
  };

  chatSocket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    // Verifica se os dados estão corretos
    if (!data.user1 || !data.user2) {
      console.error("❌ Erro: user1 ou user2 está indefinido no WebSocket!");
      return;
    }

    console.log(`📩 Mensagem recebida de ${data.user1}:`, data.message);

    let remetente = data.user1;
    let destinatario = data.user2;

    // Evita adicionar a mensagem ao chat-log se for do próprio usuário
    if (remetente !== window.user1) {
      console.log(
        `📌 Adicionando mensagem no chat-log de ${remetente} -> ${destinatario}`
      );
      addMessageToChatLog(remetente, destinatario, data.message, "received");
    } else {
      console.log(`📌 Ignorando a própria mensagem de ${remetente}`);
    }
  };

  chatSocket.onclose = function (event) {
    console.warn(
      `⚠️ WebSocket para ${user1} e ${user2} foi fechado. Código: ${event.code}, Motivo: ${event.reason}`
    );

    if (!event.wasClean || event.code !== 1000) {
      console.warn(`🚨 Conexão caiu inesperadamente! Tentando reconectar...`);
      setTimeout(() => conectarWebSocket(user1, user2), 3000);
    } else {
      console.log(`ℹ️ WebSocket fechou normalmente. Nenhuma ação necessária.`);
      setTimeout(() => conectarWebSocket(user1, user2), 1000);
    }
  };
}

// Função para enviar mensagens pelo WebSocket
function sendMessage(user1, user2, message) {
  if (
    !window.chatSockets[user2] ||
    window.chatSockets[user2].readyState !== WebSocket.OPEN
  ) {
    console.error(
      `❌ WebSocket não está aberto para ${user2}. Tentando reconectar...`
    );
    conectarWebSocket(user1, user2);
    setTimeout(() => sendMessage(user1, user2, message), 1000); // Tenta reenviar após 1s
    return;
  }

  console.log(`📤 Enviando mensagem de ${user1} para ${user2}:`, message);

  window.chatSockets[user2].send(
    JSON.stringify({
      message: message,
      user1: user1,
      user2: user2,
    })
  );

  // ✅ Só adiciona a mensagem ao chat-log se foi enviada pelo usuário logado
  if (user1 === window.user1) {
    addMessageToChatLog(user1, user2, message, "sent");
  }
}

// Função para adicionar mensagens ao chat-log corretamente
function addMessageToChatLog(user1, user2, message, type) {
  let chatLog =
    document.getElementById(`chat-log-${user2}-${user1}`) ||
    document.getElementById(`chat-log-${user1}-${user2}`);

  if (!chatLog) {
    console.error(`❌ Erro: chat-log não encontrado para ${user2}-${user1}.`);
    return;
  }

  // Verificar se a mensagem já foi adicionada (com base no conteúdo da última mensagem)
  let lastMessage = chatLog.lastElementChild;
  if (lastMessage && lastMessage.textContent === `${user1}: ${message}`) {
    console.log("⚠️ Mensagem duplicada detectada. Ignorando...");
    return;
  }

  const messageElement = document.createElement("div");
  messageElement.classList.add(
    type === "sent" ? "sent-message" : "received-message"
  );
  messageElement.textContent = `${user1}: ${message}`;
  chatLog.appendChild(messageElement);
  chatLog.scrollTop = chatLog.scrollHeight;
}

// Adicionar evento para enviar mensagem ao pressionar Enter
document.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    let activeInput = document.activeElement;
    if (activeInput && activeInput.classList.contains("chat-input")) {
      event.preventDefault();

      let chatBox = activeInput.closest(".chat-window");
      let user1 = window.user1;
      let user2 = chatBox ? chatBox.dataset.username : null;

      if (!user1 || !user2) {
        console.error(
          "❌ Erro: user1 ou user2 não está definido corretamente ao enviar mensagem."
        );
        return;
      }

      let message = activeInput.value.trim();

      if (message !== "") {
        console.log(`📤 Enviando mensagem de ${user1} para ${user2}:`, message);
        sendMessage(user1, user2, message);
        activeInput.value = "";
      }
    }
  }
});

// Lista de usuários fictícios (simulando dados do backend)
let usuariosOnline = ["fulano_a", "fulano_b", "fulano_c"];

// Preencher a lista de conversas no Messenger
function carregarUsuariosNaLista() {
  let chatList = document.getElementById("chat-list");

  if (!chatList) {
    console.error("❌ Erro: Elemento #chat-list não encontrado!");
    return;
  }

  chatList.innerHTML = ""; // Limpa a lista antes de adicionar novos usuários

  usuariosOnline.forEach((user) => {
    let userElement = document.createElement("p");
    userElement.textContent = user;
    userElement.dataset.username = user;
    userElement.style.cursor = "pointer";
    userElement.addEventListener("click", function () {
      let user2 = this.dataset.username;
      abrirJanelaChat(window.user1, user2);
      conectarWebSocket(window.user1, user2);
    });

    chatList.appendChild(userElement);
  });

  console.log("✅ Lista de usuários carregada.");
}

// Chama a função ao carregar a página
document.addEventListener("DOMContentLoaded", function () {
  carregarUsuariosNaLista();
});

# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Pratique manipulação de strings, listas, laços de repetição, condicionais e entrada de dados criando uma versão interativa do jogo da Forca no terminal.

## 📝 Tarefas

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Crie um jogo de terminal que escolha uma palavra aleatoriamente de uma lista predefinida. O jogador deve descobrir a palavra sugerindo uma letra por vez, antes de atingir o limite de tentativas incorretas.

#### Requisitos
O programa concluído deve:

- Escolher aleatoriamente uma palavra de uma lista predefinida usando o módulo `random`.
- Definir um limite de tentativas incorretas e acompanhar os palpites e erros durante a partida.
- Exibir cada letra ainda não descoberta como um espaço reservado e revelar as letras acertadas nas posições correspondentes. Por exemplo, para `python`, após acertar `p` e `t`, exiba `p _ t _ _ _`.
- Solicitar um palpite de uma única letra por rodada e informar se ela aparece na palavra.
- Não descontar tentativas por entradas inválidas ou letras já tentadas; descontar uma tentativa apenas quando o jogador errar uma letra válida.
- Exibir as tentativas incorretas restantes e continuar até que todas as letras sejam descobertas ou o limite de erros seja atingido.
- Informar se o jogador venceu ou perdeu e revelar a palavra escolhida ao encerrar a partida.

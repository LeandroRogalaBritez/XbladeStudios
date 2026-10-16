# Política geral no Google Play

A Xblade Studios utilizará **um único endereço de Política de Privacidade para seus jogos**. No GitHub Pages deste projeto, o endereço esperado é `https://leandrorogalabritez.github.io/XbladeStudios/privacidade/`, disponível após a primeira implantação bem-sucedida.

O documento identifica o estúdio e descreve, em linguagem direta, dados locais, Google AdMob/UMP, Unity quando utilizada, Steam, site e suporte, compartilhamento, segurança, retenção e direitos. As diferenças de cada versão estão descritas por serviços e plataformas; o catálogo em `/jogos/` informa os jogos, as plataformas e os serviços verificados. Android é gratuito com AdMob e sem compras internas nas versões atuais; serviços e transações Steam ficam na plataforma.

O site inteiro também está disponível em inglês. A política equivalente fica em `https://leandrorogalabritez.github.io/XbladeStudios/en/privacy/` e os termos em `/en/terms/`. O seletor PT-BR / EN preserva a página; cada documento pode ser lido diretamente, sem login, JavaScript ou escolha prévia de idioma. A URL portuguesa existente permanece válida.

O Google exige que a política seja aplicável ao app, identifique o desenvolvedor ou o aplicativo e divulgue suas práticas. Essa organização compartilhada foi escolhida para facilitar a manutenção dos jogos do mesmo estúdio. Não é uma dispensa de descrever diferenças ou atualizar o texto quando houver mudanças.

## Publicar e cadastrar

1. Revise os textos e o comportamento do APK/AAB final, incluindo SDKs, permissões, consentimento e diagnósticos.
2. Ative GitHub Pages com origem **GitHub Actions** e execute o workflow conforme o README. Ele publica o pacote gerado, com os caminhos ajustados ao projeto.
3. Abra `https://leandrorogalabritez.github.io/XbladeStudios/privacidade/` sem login, após a implantação. Valide SSL, HTTP 200, HTML legível e acesso em outras redes/regiões. Se configurar domínio próprio, use o endereço final mostrado no deploy seguido de `/privacidade/`.
4. Mantenha o site público, sem senha, restrição por país ou bloqueio de leitura. A privacidade do repositório é diferente da visibilidade do site.
5. No Play Console de cada jogo abrangido, use **Políticas e programas → Conteúdo do app → Política de Privacidade → Iniciar/Gerenciar** e informe a URL geral publicada.
6. Confira o link na página de detalhes e mantenha Segurança dos dados, Contém anúncios e público-alvo coerentes com cada aplicativo.

Não use localhost, 127.0.0.1, um PDF ou endereço ilustrativo. O complemento `/privacidade/admob/` não substitui o documento completo.

## Link dentro dos jogos: ainda pendente

Cada jogo deve apresentar um item **Política de Privacidade** sempre acessível, apontando para a mesma URL geral publicada. Não condicione esse item à disponibilidade de anúncio ou ao consentimento UMP.

Os controles existentes “Privacidade dos anúncios” ou “Opções de privacidade” abrem apenas as escolhas de consentimento. Eles devem continuar separados do link da política.

Pontos identificados para integração depois que houver domínio de produção:

| Projeto | Ponto de interface | Ação |
| --- | --- | --- |
| Purr Box | `scripts/ui/options_panel.gd` | Botão sempre visível chamando `OS.shell_open()` com a URL geral. |
| Normal Dev Guy | Menu principal/opções; não depender de `Ads/AdPrivacyButton.cs` | Botão independente chamando `Application.OpenURL()` com a URL geral. |
| Alerta: Terra | `scenes/invasion/invasion_hud.gd`, menu/pausa | Novo acesso à política, independente do botão condicional que chama UMP. |

Os projetos dos jogos foram apenas lidos. Nenhum domínio fictício ou endereço local foi inserido neles.

Teste o acesso no APK/AAB de produção, antes e depois de mensagens de consentimento e com anúncio indisponível. O usuário não deve precisar criar uma conta para ler o documento.

## Novos jogos

Se o novo jogo mantiver as práticas já descritas, ele pode apontar para a mesma política. Acrescente-o ao catálogo na plataforma correta e confirme os serviços no inventário técnico.

Se introduzir novos SDKs, mediação, contas, compras dentro do app, backend, tratamento de outros dados ou direcionamento infantil, revise a política e os fluxos **antes** de distribuí-lo. Não declare ausência de coleta por ser um jogo simples.

O usuário confirmou apenas AdMob e que seus jogos não são direcionados a crianças. Classificação indicativa “Livre” e seleção de público-alvo no Play Console são configurações diferentes. Não foi inventada uma idade mínima.

## Verificações externas pendentes

- Disponibilidade pública mundial, HTTPS e headers no domínio real.
- URL geral dentro dos apps e cadastrada no Play Console.
- SDKs, permissões e tráfego dos binários de produção.
- Configuração real dos painéis AdMob/UMP, Unity e Steam.
- Coerência dos formulários de dados de cada jogo.
- Critérios operacionais de retenção e exclusão das mensagens de suporte.

Não há contas próprias de jogador nas versões examinadas. Se passarem a existir, implemente os fluxos de exclusão exigidos pelas lojas e revise o documento.

## Fontes

Consultadas em 15/10/2026:

- [Google Play: dados do usuário e conteúdo da Política de Privacidade](https://support.google.com/googleplay/android-developer/answer/10144311?hl=pt-BR).
- [Google Play: informar a URL e preparar a revisão](https://support.google.com/googleplay/android-developer/answer/9859455?hl=pt-BR#privacy_policy).
- [Mobile Ads SDK: dados](https://developers.google.com/admob/android/privacy/play-data-disclosure).
- [Google UMP](https://developers.google.com/admob/unity/privacy).
- [Unity: dados do runtime](https://unity.com/legal/developer-privacy-policy-faq).
- [Valve: privacidade](https://store.steampowered.com/privacy_agreement/?l=brazilian).

A estrutura local não comprova aprovação pelas lojas ou disponibilidade pública.

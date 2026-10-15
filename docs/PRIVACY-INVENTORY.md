# Inventário técnico para manutenção

Revisão de fontes em 15/10/2026. Este arquivo ajuda a manter a política geral e o catálogo; não é uma política pública nem uma inspeção completa dos binários e dos painéis.

| Projeto | Plataforma divulgada | Componentes verificados |
| --- | --- | --- |
| Caixa de Ronrons / Purr Box | PC/Steam e Android | Salvamento e preferências locais; Steam no desktop; AdMob recompensado/UMP apenas Android. |
| Normal Dev Guy — Inside Kenney World | PC/Steam e Android | save.json, PlayerPrefs e frequência de anúncios locais; Steam no desktop; AdMob intersticial/UMP apenas Android; runtime Unity. |
| Alerta: Terra | Somente Android, conforme pedido do usuário | Recordes de pontuação e ondas em arquivo local; AdMob intersticial e recompensado, UMP e ponte de autorização de anúncio. |

## Fontes locais examinadas

- Purr Box: `E:/Godot Projetos/meus projetos/purr-box`, scripts de anúncios, opções, salvamento, SteamBridge, projeto e configuração Android. Pacote `com.xbladestudios.purrbox`. Sem criação de conta própria, login, billing ou servidor de analytics identificados nos scripts revisados. O arquivo de progresso tem criptografia/verificação de integridade; não presume o mesmo mecanismo para preferências.
- Normal Dev Guy: `E:/Unity/UnityProjetos/ProjectFat`, scripts Ads, Save, SteamWorks, Packages/manifest.json e ProjectSettings. Pacote `com.xbladestudios.normaldevguykenneyworld`. Mobile Ads Unity 11.5.0. O projeto contém submitAnalytics: 1; serviços de nuvem desabilitados não provam ausência de dados do runtime. Confira a configuração e o tráfego da versão enviada.
- Alerta: Terra: `E:/Godot Projetos/meus projetos/alerta-terra`, project.godot, export_presets.cfg, platform_services.gd, admob_provider.gd, configurações de produção/teste, invasion_hud.gd e survival_records.gd. Pacote oficial `com.xbladestudios.alertaterra`. Recordes em `user://survival_records.json`. A variante Android usa Google Mobile Ads e UMP via Poing Studios, sem cadastro próprio ou chamadas próprias para servidor de gameplay identificadas. Há variantes web/Poki no projeto, mas não são divulgadas no catálogo nem abrangidas como integração ativa nesta política, conforme escopo Android dado pelo usuário.

Os IDs públicos de anúncios encontrados no código não foram usados para deduzir um app-ads.txt. As linhas devem vir das contas/redes.

## Quando acrescentar jogos

Registre plataforma, pacote, serviços ativos, dados locais, permissões, destinatários, consentimento, contas e compras. Atualize o detalhe de serviços no cartão de cada plataforma. Se o comportamento não estiver descrito na política geral, revise-a antes da distribuição. Não copie a declaração de um jogo para outro sem conferir os componentes.

As mensagens de suporte usam o Gmail público já divulgado. Os critérios operacionais de conservação devem ser confirmados pelo responsável. Os jogos e seus painéis não foram modificados nesta entrega.

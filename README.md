# Xblade Studios

Site institucional estático em português brasileiro, com catálogo por plataforma, suporte e uma Política de Privacidade geral para os jogos do estúdio. HTML, CSS e um pequeno script de menu móvel; sem framework, npm, banco de dados ou build.

**Estado: prévia local para revisão, sem publicação pública.** Os jogos permanecem em seus próprios repositórios. Nenhum projeto de jogo foi modificado nesta entrega.

## Visualizar e verificar

Na pasta deste projeto:

```powershell
python tools/preview.py
```

Abra <http://127.0.0.1:4173>. Para outra porta: `python tools/preview.py --port 8080`. Encerre com Ctrl+C. Python é usado apenas na prévia; não é necessário na hospedagem. Evite abrir por file:// porque os caminhos começam na raiz.

```powershell
python tools/check.py
node --check public/assets/site.js
```

A verificação Python confere HTML, links internos, âncoras, assets e metadados. Node é opcional e verifica apenas a sintaxe do menu.

## Organização

```text
public/                         ← pasta publicada diretamente
  index.html                    ← marca, apresentação e entrada para plataformas
  jogos/index.html              ← catálogo PC/Steam e Android
  suporte/index.html            ← atendimento para os jogos do estúdio
  privacidade/index.html        ← política geral usada pelos jogos
  privacidade/site/index.html   ← política do site institucional
  privacidade/admob/index.html  ← complemento sobre publicidade
  privacidade/purr-box/          ← endereço antigo preservado
  privacidade/normal-dev-guy/    ← endereço antigo preservado
  exclusao-de-dados/index.html   ← orientações gerais sobre dados
  termos/index.html
  404.html
  assets/                       ← marca, estilos, script e imagens locais
  _headers                      ← segurança e cache
  _redirects                    ← caminhos antigos → política geral no Pages
  robots.txt                    ← prévia; permite políticas e assets
tools/                          ← servidor e verificação, fora da publicação
docs/                           ← fontes, inventário técnico e pendências
```

As páginas são HTML pronto, sem dependência de JavaScript para ler políticas ou catálogo. As seções de plataforma usam links para âncoras; não há filtros que dependam de script.

## Atualizar o catálogo e adicionar jogos

Edite **`public/jogos/index.html`**. O conteúdo está agrupado nas seções `#pc` e `#android`. Para adicionar um título:

1. Copie um `article.game-card` para cada plataforma em que pretende oferecê-lo.
2. Ajuste título, subtítulo, descrição, arte e texto alternativo. Use imagens locais otimizadas, com dimensões declaradas.
3. Informe apenas sites e URLs de loja reais. Se a página da loja não existir, mantenha um status de preparação, sem botão de download fictício.
4. No detalhe “Serviços e privacidade nesta versão”, descreva os componentes reais daquela plataforma. Não presuma que as versões PC e Android tratam os mesmos dados.
5. Se houver um serviço ou tratamento novo, atualize a política **antes** de distribuir o jogo.
6. Execute a verificação e confira a página no celular.

Alerta: Terra está apenas em Android por orientação do usuário. As versões Android estão identificadas como em preparação porque não foram fornecidos links públicos de Google Play. Os dois sites comerciais existentes permanecem separados e vinculados no catálogo.

A apresentação institucional, o suporte, as orientações de dados e a política usam “jogos da Xblade Studios”, sem lista fixa de títulos. Novos nomes e plataformas ficam no catálogo.

## Manutenção da política geral

A URL a ser usada pelos jogos, depois de publicar, será **o domínio real + `/privacidade/`**. A página identifica a Xblade Studios e descreve dados locais, anúncios, Unity, Steam, suporte, compartilhamento, segurança, retenção e direitos.

Ela se aplica aos jogos do estúdio que a vinculam, com as diferenças dos serviços e plataformas descritas no texto e no catálogo. **Não cobre automaticamente uma funcionalidade desconhecida só porque o jogo pertence ao estúdio.** Se acrescentar cadastro, compras dentro do app, novos SDKs, mediação, nuvem própria ou público infantil, revise a política, o jogo e as declarações das lojas antes de lançar.

Veja `docs/PRIVACY-INVENTORY.md` para os componentes verificados e `docs/GOOGLE-PLAY.md` para cadastrar o endereço e incluir o link dentro dos apps.

Os caminhos antigos por jogo continuam existindo. No Cloudflare Pages, `_redirects` os encaminha para `/privacidade/` por HTTP 301. Na prévia Python, eles apresentam um link para a política geral. Não cadastre esses caminhos em novos apps.

A política do **site** fica separada em `/privacidade/site/`, pois navegar pelo site é diferente de executar os SDKs dos jogos.

## Identidade, contato e arquivos

- Cores e layouts: `public/assets/style.css`. Símbolo proposto: `brand.svg`.
- Artes e origens: `docs/ASSETS.md`. Os originais dos projetos dos jogos não foram alterados.
- E-mail público recuperado do site existente: `leandrorogalabritezltda@gmail.com`. Confirme se continua sendo o canal desejado.
- Não foram inventados perfis sociais; há um link para o desenvolvedor na Steam. Acrescente redes confirmadas na área `.socials`.
- Cabeçalhos e rodapés estão em HTML nas páginas. Uma mudança nesses componentes deve ser replicada em todas elas.
- Títulos, descrições e imagem social local estão definidos. Depois de escolher o domínio, configure URLs absolutas para `og:image`, `og:url` e canonical.
- Ao alterar o CSS, atualize o sufixo `?v=` das referências nas páginas para evitar uma cópia antiga no cache.

O código do site não utiliza analytics, anúncios, cookies opcionais, armazenamento do navegador, formulário, fontes externas ou vídeos incorporados.

## GitHub e Cloudflare Pages

O Git local foi inicializado na branch `main`, sem commit. Nenhum remoto foi criado e nenhum push foi feito. Crie um repositório próprio para o site e, depois de revisar os arquivos:

```powershell
git add .
git commit -m "Cria site da Xblade Studios"
git remote add origin URL_REAL_DO_SEU_REPOSITORIO
git push -u origin main
```

Substitua a instrução em maiúsculas pela URL real. Não inclua credenciais no repositório; .env, caches e artifacts estão ignorados.

No painel Cloudflare: **Workers & Pages → Create application → Pages → Import an existing Git repository**. Conecte o GitHub e escolha esse repositório.

| Configuração | Valor |
| --- | --- |
| Branch | `main` |
| Preset | None |
| Comando de build | `exit 0` |
| Diretório de saída | `public` |
| Diretório raiz | raiz do repositório |

A publicação ocorrerá em um subdomínio `pages.dev` retornado pelo painel, sujeito à disponibilidade. Nenhum endereço foi reservado nesta entrega. O plano gratuito tem [limites](https://developers.cloudflare.com/pages/platform/limits/); domínio próprio tem registro e renovação separados.

Commits na branch conectada geram novas publicações. Use branch/PR para revisar preview antes de integrar em main. Previews de hospedagem não são automaticamente privados. Robots e noindex também não protegem o acesso.

Para domínio próprio, use **Custom domains** no projeto Pages e siga o [guia de DNS](https://developers.cloudflare.com/pages/configuration/custom-domains/). Mantenha o endereço de privacidade estável ao mudar de hospedagem.

## Verificar antes da publicação

- Aprove o visual e os textos; confirme contato e a operação de retenção/exclusão de mensagens.
- Confira os SDKs, permissões e tráfego do APK/AAB real e das versões PC. Os arquivos foram examinados, mas os painéis e os binários de produção não foram auditados integralmente.
- Escolha o domínio, configure metadados absolutos e revise avisos de prévia/indexação das páginas aprovadas.
- Abra a política HTTPS sem login e valide certificado, resposta 200 e leitura do documento em outras redes/regiões. Não ative senha, Access ou restrições por país.
- Cadastre a mesma URL geral nas lojas de cada jogo abrangido e dentro de cada app. Os botões de consentimento UMP não substituem o link da política.
- Confira rotas diretas, âncoras, 404 e headers no domínio real. Não use fallback de SPA.
- O servidor Python não simula `_headers` ou `_redirects`; valide ambos no Pages.

## app-ads.txt

**O arquivo ainda não existe**, porque as linhas oficiais da conta não foram fornecidas. Não há publisher IDs fictícios nem um arquivo vazio apresentado como válido.

Copie o trecho personalizado do painel AdMob e as linhas de eventuais redes usadas, sem deduzir IDs a partir de outro arquivo. Crie `public/app-ads.txt` em UTF-8. Ele ficará na raiz do domínio, em `/app-ads.txt`, com header de texto simples já preparado.

Depois de publicar, abra a URL e confira HTTP 200, texto real e ausência de HTML, login ou bloqueio do rastreador. Cadastre o **site do desenvolvedor** nas lojas e acompanhe a verificação no AdMob; o domínio informado nas lojas permite a descoberta do arquivo. [Guia oficial](https://support.google.com/admob/answer/9363762?hl=en-GB).

## Fontes oficiais

Consulta em **15 de outubro de 2026**:

- [Cloudflare Pages: HTML estático](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).
- [Cloudflare Pages: limites](https://developers.cloudflare.com/pages/platform/limits/).
- [Cloudflare Pages: redirecionamentos](https://developers.cloudflare.com/pages/configuration/redirects/).
- [Cloudflare Pages: domínios](https://developers.cloudflare.com/pages/configuration/custom-domains/).
- [Cloudflare: privacidade](https://www.cloudflare.com/privacypolicy/).
- [Google Play: política de dados do usuário](https://support.google.com/googleplay/android-developer/answer/10144311?hl=pt-BR).
- [Google Play: preparar o app e informar a política](https://support.google.com/googleplay/android-developer/answer/9859455?hl=pt-BR#privacy_policy).
- [AdMob: divulgação de dados](https://developers.google.com/admob/android/privacy/play-data-disclosure).
- [AdMob: UMP](https://developers.google.com/admob/unity/privacy).
- [AdMob: app-ads.txt](https://support.google.com/admob/answer/9363762?hl=en-GB).
- [Unity: política dos jogadores](https://unity.com/legal/game-player-and-app-user-privacy-policy).
- [Valve: política de privacidade](https://store.steampowered.com/privacy_agreement/?l=brazilian).
- [Apple: privacidade](https://developer.apple.com/app-store/review/guidelines/#privacy) e [exclusão de contas](https://developer.apple.com/support/offering-account-deletion-in-your-app/), caso futuramente haja versão iOS.

As políticas devem acompanhar a operação real e as leis dos países atendidos. Revisão jurídica pode ajustar os textos. Não há promessa de conformidade ou aprovação automática pelas lojas.

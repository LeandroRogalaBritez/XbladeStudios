# Estado da entrega — 15/10/2026

Site em HTML, CSS e JavaScript mínimo, com versões completas PT-BR e EN. Remoto GitHub `LeandroRogalaBritez/XbladeStudios`, branch `main`. O repositório está público e GitHub Pages está ativo. A execução `38833639146` implantou a versão anterior com sucesso; esta atualização simplifica os documentos e acrescenta o site em inglês.

## Estrutura atual

- Apresentação institucional sem lista fixa de títulos.
- Catálogo separado em `/jogos/`, organizado por PC/Steam e Android.
- Alerta: Terra incluído apenas em Android, conforme orientação do usuário, embora o projeto também possua variantes técnicas para outras plataformas.
- Uma política em `/privacidade/` e sua equivalente `/en/privacy/`, reunindo jogos, site e suporte em sete seções. O texto em português passou de 1.675 para 687 palavras.
- Termos em `/termos/` e `/en/terms/`, para jogos Android gratuitos com AdMob e sem compras internas nas versões atuais, remetendo serviços e transações Steam à plataforma.
- Inicial, catálogo, suporte, orientações sobre dados e páginas de compatibilidade traduzidos. Seletor de idioma preserva a página equivalente e funciona sem JavaScript.
- Caminhos antigos de privacidade preservados com redirecionamento HTML no pacote do GitHub Pages e link acessível sem JavaScript.
- As versões Android estão identificadas como em preparação; não foram fornecidas URLs públicas de Google Play.
- Artes copiadas e otimizadas dos próprios projetos. Originais e projetos dos jogos permanecem intactos.

## Informações confirmadas

Nome do estúdio e uso somente de AdMob, sem outras redes de mediação, confirmados pelo usuário. Os jogos não são direcionados especificamente a crianças. Não foi criada uma idade mínima.

A revisão de fontes dos três jogos identificou os componentes e as diferenças registrados em `PRIVACY-INVENTORY.md`. A política geral não depende de enumerar esses títulos e não afirma que todo jogo usa todos os serviços.

## Pendências

- [ ] Aprovar identidade e textos; confirmar contato, responsável e a operação de retenção/exclusão de mensagens.
- [ ] Verificar SDKs, permissões e tráfego dos binários de produção, incluindo diagnósticos da Unity.
- [ ] Obter links públicos das versões Android quando estiverem disponíveis.
- [x] Preparar workflow GitHub Actions com validação, pacote estático e implantação Pages.
- [x] Gerar caminhos para subdiretório, metadados absolutos, sitemap e indexação no pacote de produção.
- [x] Pages ativado e repositório público, verificados após configuração pelo usuário.
- [x] Primeira implantação bem-sucedida no GitHub; site em `https://leandrorogalabritez.github.io/XbladeStudios/`.
- [ ] Verificar HTTPS, leitura sem login e acesso por outras redes/regiões.
- [ ] Inserir a mesma URL geral de privacidade dentro de cada app e cadastrá-la nas lojas.
- [ ] Conferir consentimento e declarações por aplicativo nos painéis.
- [ ] Receber as linhas reais de app-ads.txt e validar o arquivo/painel depois de publicar.

Os testes locais não comprovam disponibilidade mundial, aprovação de loja ou comportamento do binário de produção. Não foram alterados os painéis nem os projetos dos jogos.

## Verificação da estrutura geral

- Onze páginas passaram na verificação de links internos, âncoras, assets, idioma e metadados; JavaScript passou na verificação de sintaxe.
- Inicial, catálogo, política geral, suporte, exclusão e caminhos antigos abriram em HTML com HTTP 200 na prévia.
- O catálogo contém dois cartões PC/Steam e três Android; Alerta: Terra não aparece em PC.
- As artes carregaram sem falhas. O acesso por âncora à seção Android e o detalhe de serviços de Alerta: Terra funcionaram.
- Catálogo conferido visualmente em 1440 px e 390 px. Inicial, catálogo e política geral foram verificados em 320 px sem rolagem horizontal.
- As páginas institucionais e a política geral não contêm lista fixa de títulos. Os nomes aparecem no catálogo.
- Captura do catálogo Android: `artifacts/catalog-android.jpg`, fora da pasta publicada.
- O GitHub Pages não oferece `_headers` ou regras `_redirects` personalizadas. O pacote usa CSP por meta tag e redirecionamentos HTML; as antigas URLs não retornam um HTTP 301 personalizado.
- Testes de publicação cobrem a raiz de domínio e `/Studio/`, assets da 404, URLs antigas, sitemap, exclusão de arquivos internos e proteção dos arquivos de origem.
- `app-ads.txt` exige a raiz do domínio; o prefixo `/XbladeStudios/` não atende essa descoberta. Alternativas documentadas no README.

## Primeira execução no GitHub

Workflow enviado para `main` no commit `c7a0ea0`. A [execução 38833385749](https://github.com/LeandroRogalaBritez/XbladeStudios/actions/runs/38833385749) passou na validação de páginas e nos seis testes em Ubuntu/Python 3.13. A preparação parou em `actions/configure-pages` porque o site Pages não existe/está desativado (API retornou `Not Found`). O deploy não foi executado.

Ative **Settings → Pages → Source: GitHub Actions**, com plano/visibilidade compatíveis, e execute o workflow manualmente. O navegador disponível estava sem sessão GitHub; nenhuma configuração da conta ou visibilidade foi alterada. O pacote também foi conferido localmente em `/XbladeStudios/`: imagens e estilos carregaram, a URL antiga encaminhou à política geral e a 404 em rota profunda retornou ao início corretamente.

## Atualização de idioma e simplificação

Estado posterior: Pages ativo, repositório público e primeira implantação concluída (`38833639146`). A política única mantém as informações de coleta pelo AdMob e pelos componentes realmente identificados, sem acrescentar serviços do site usado como referência. Os antigos documentos separados de site e AdMob apresentam links às seções correspondentes da política única.

As 22 páginas passaram na validação estática. Oito testes cobrem, além da publicação, traduções ausentes, idioma incorreto, links recíprocos PT-BR/EN, alternates absolutos, 404 inglesa fora da indexação e redirecionamentos antigos em inglês. Inicial, política e catálogo foram conferidos em 320 px; o seletor permanece acessível com o menu móvel fechado. O menu em inglês abre com “Close” e fecha por Escape.

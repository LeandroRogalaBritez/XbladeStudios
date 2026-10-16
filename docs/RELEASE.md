# Estado da entrega — 15/10/2026

Site em HTML, CSS e JavaScript mínimo. Remoto GitHub `LeandroRogalaBritez/XbladeStudios`, branch `main`. Publicação preparada por GitHub Actions; o repositório foi encontrado privado e com Pages desativado. A primeira implantação depende da ativação do Pages e da compatibilidade do plano/visibilidade.

## Estrutura atual

- Apresentação institucional sem lista fixa de títulos.
- Catálogo separado em `/jogos/`, organizado por PC/Steam e Android.
- Alerta: Terra incluído apenas em Android, conforme orientação do usuário, embora o projeto também possua variantes técnicas para outras plataformas.
- Uma política geral dos jogos em `/privacidade/`, com seções por serviços e plataforma.
- Política do site separada; suporte e orientações sobre dados falam dos jogos do estúdio.
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
- [ ] Ativar Pages com origem GitHub Actions; confirmar plano compatível com repositório privado ou autorizar mudança de visibilidade.
- [ ] Confirmar primeira implantação e endereço final no GitHub.
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

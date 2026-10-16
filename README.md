# Xblade Studios

Site institucional em português brasileiro e inglês, com catálogo por plataforma, suporte, Política de Privacidade e Termos de Uso. HTML, CSS e JavaScript mínimo, sem npm, framework ou banco de dados. Hospedagem: **GitHub Pages**, com publicação por GitHub Actions.

Repositório: [LeandroRogalaBritez/XbladeStudios](https://github.com/LeandroRogalaBritez/XbladeStudios).

## Ativar a primeira publicação

1. Abra **Settings → Pages → Build and deployment → Source → GitHub Actions**.
2. Para repositórios privados, Pages exige um plano compatível. No GitHub Free, exige repositório público; mudar a visibilidade também expõe código e histórico. O workflow não altera essa configuração. Neste projeto, o Pages já foi ativado e o repositório está público.
3. Envie os arquivos para `main`. Se o commit já estiver no GitHub, abra **Actions → Publicar site no GitHub Pages → Run workflow → main → Run workflow**.
4. Aguarde os três jobs: verificar, preparar e publicar. O job de publicação mostra o endereço final. Se houver uma regra de aprovação do ambiente `github-pages`, aprove a implantação no painel.
5. Confira o site e a política sem login, HTTPS, links, imagens e uma URL inexistente.

Endereços esperados, sem domínio personalizado:

- [Site](https://leandrorogalabritez.github.io/XbladeStudios/).
- [Política para os jogos e Google Play](https://leandrorogalabritez.github.io/XbladeStudios/privacidade/).
- [Configuração Pages](https://github.com/LeandroRogalaBritez/XbladeStudios/settings/pages).
- [Execuções do workflow](https://github.com/LeandroRogalaBritez/XbladeStudios/actions/workflows/pages.yml).

Esses endereços só ficam ativos após uma implantação bem-sucedida. Depois de verificar o acesso público, use a URL da política no Play Console e dentro de cada jogo abrangido. Veja [o roteiro Google Play](docs/GOOGLE-PLAY.md).

## Atualizações automáticas

`.github/workflows/pages.yml` executa em pushes para `main` que alterem o site, ferramentas, testes ou workflow. Também aceita execução manual. Pull requests executam somente a validação.

Usa ações oficiais do GitHub para configurar Pages, enviar o artefato e publicar. O token recebe leitura do repositório; somente o job de implantação recebe `pages: write` e `id-token: write`. Não exige token pessoal, segredo ou conta Cloudflare.

`tools/prepare_pages.py` gera `artifacts/pages` a partir de `public/`:

- Adapta links e assets ao prefixo `/XbladeStudios/` retornado pelo Pages, inclusive na 404.
- Define canonical, `og:url` e `og:image` absolutos, sitemap, robots e `.nojekyll`.
- Remove avisos de prévia e `noindex` das páginas publicadas; mantém 404 e endereços antigos fora da indexação.
- Preserva URLs antigas de política com redirecionamento HTML e link para a política geral. Pages não oferece regras `_redirects`/301 personalizadas.
- Aplica CSP por meta tag. GitHub Pages controla os cabeçalhos HTTP; `_headers` não é enviado.
- Envia somente os arquivos do site. Documentação, testes, ferramentas e capturas ficam fora do artefato.

A origem continua própria para prévia local. O pacote não altera `public/` e exige uma saída nova ou vazia, para não apagar arquivos existentes. Não publique `public/` diretamente por uma branch: use o artefato do workflow.

Para domínio próprio, configure **Settings → Pages → Custom domain**, ajuste o DNS conforme o GitHub e execute o workflow novamente. O endereço é obtido da configuração Pages. Atualize os links nos apps se mudar a URL.

## Visualizar e verificar

```powershell
python tools/preview.py
```

Abra [http://127.0.0.1:4173](http://127.0.0.1:4173). Encerre com Ctrl+C. Outra porta: acrescente `--port 8080`. Não abra por `file://`, pois os caminhos começam na raiz.

```powershell
python tools/check.py
python -m unittest discover -s tests -v
node --check public/assets/site.js
```

Python 3.10 ou superior; o workflow usa 3.13. Node é opcional, para verificar a sintaxe do menu. Os testes cobrem links, âncoras, assets, metadados, publicação em subdiretório e domínio próprio, 404 e URLs antigas.

Simule o pacote Pages usando uma pasta de saída nova:

```powershell
python tools/prepare_pages.py --base-url https://leandrorogalabritez.github.io/XbladeStudios --output artifacts/pages-local
python tools/check.py --root artifacts/pages-local --base-path /XbladeStudios --production
python tools/preview.py --directory artifacts/pages-local --base-path /XbladeStudios --port 4174
```

Abra [http://127.0.0.1:4174/XbladeStudios/](http://127.0.0.1:4174/XbladeStudios/). Para repetir, escolha outra saída vazia. A prévia não comprova disponibilidade pública nem simula os cabeçalhos do GitHub.

## Organização e manutenção

| Caminho | Conteúdo |
| --- | --- |
| `public/index.html` | Apresentação do estúdio |
| `public/jogos/index.html` | Catálogo PC/Steam e Android |
| `public/privacidade/index.html` | Política geral dos jogos |
| `public/privacidade/site/`, `admob/` | Links de compatibilidade para as seções da política geral |
| `public/privacidade/purr-box/`, `normal-dev-guy/` | URLs antigas |
| `public/suporte/`, `exclusao-de-dados/`, `termos/` | Páginas institucionais |
| `public/assets/` | Marca, estilos, menu e imagens |
| `public/en/` | Versão completa do site em inglês |
| `tools/`, `tests/` | Prévia, pacote e verificações |
| `docs/` | Créditos das artes e orientações de publicação |
| `artifacts/` | Saídas e capturas ignoradas pelo Git |

O código do site não usa analytics, anúncios, cookies opcionais, formulários, contas, armazenamento do navegador, fontes externas ou vídeos incorporados. A infraestrutura Pages pode tratar dados técnicos das requisições conforme sua política.

Para adicionar um jogo, copie um `article.game-card` no catálogo nas plataformas corretas, informe arte e URLs reais e descreva os serviços daquela versão. Alerta: Terra aparece apenas em Android. Lançamentos Android permanecem em preparação enquanto não houver links públicos de loja.

A política geral se aplica aos jogos que a vinculam e às práticas descritas. Novos SDKs, mediação, contas, compras, nuvem própria ou direcionamento infantil exigem revisão antes do lançamento. Confira as [orientações de publicação](docs/GOOGLE-PLAY.md) e teste o link dentro dos aplicativos.

Contato público: `leandrorogalabritezltda@gmail.com`. Artes em [ASSETS.md](docs/ASSETS.md). Cabeçalhos e rodapés são replicados entre páginas; atualize todas as ocorrências. Ao alterar CSS, atualize o sufixo `?v=` para evitar cache antigo.

## Idiomas e documentos

Todas as páginas têm versões PT-BR e EN. O seletor no cabeçalho abre a página equivalente, sem depender de JavaScript, cookies ou detecção automática. Os endereços em português foram preservados; inglês fica em `/en/`, com `/en/games/`, `/en/support/`, `/en/privacy/`, `/en/terms/` e `/en/data-deletion/`.

As equivalências ficam em `tools/locales.py`. Ao criar uma página, crie os dois HTMLs, registre o par e inclua os links de idioma no cabeçalho e os metadados `hreflang`. Atualize o conteúdo nos dois idiomas. A validação detecta traduções ausentes e idiomas incorretos; o pacote gera alternates absolutos com o prefixo correto do Pages. As duas versões de 404 ficam fora da indexação; a 404 automática do GitHub usa o arquivo da raiz, com seletor para inglês.

A política foi simplificada e reúne dados locais, AdMob, Steam, tecnologia Unity quando utilizada, navegação no site, suporte, segurança e exclusão. Os caminhos antigos sobre site e AdMob apontam às seções correspondentes. Os termos descrevem jogos Android gratuitos com anúncios e sem compras internas nas versões atuais. Transações e serviços Steam seguem as condições da plataforma; o site não vende ou recebe pagamentos.

URLs em inglês após implantação:

- [Site](https://leandrorogalabritez.github.io/XbladeStudios/en/).
- [Privacy Policy](https://leandrorogalabritez.github.io/XbladeStudios/en/privacy/).
- [Terms of Use](https://leandrorogalabritez.github.io/XbladeStudios/en/terms/).

## app-ads.txt no GitHub Pages

O arquivo ainda não existe: faltam as linhas oficiais do painel AdMob. Não deduza IDs nem use um arquivo vazio como configuração válida.

**O AdMob procura `/app-ads.txt` na raiz do domínio.** Neste projeto, criar `public/app-ads.txt` publicaria em `/XbladeStudios/app-ads.txt`, o que não resolve a descoberta na raiz.

Para o domínio padrão, o arquivo precisa estar em `https://leandrorogalabritez.github.io/app-ads.txt`, por meio do site de usuário no repositório `LeandroRogalaBritez.github.io`. A alternativa é atribuir um domínio próprio diretamente a este projeto; nesse caso, `public/app-ads.txt` fica na raiz desse domínio. Nenhum repositório adicional ou domínio foi criado.

Depois de receber o trecho oficial e publicar no endereço correto, confirme resposta 200, texto simples, ausência de login/bloqueio e verificação no AdMob. O site do desenvolvedor nas lojas deve permitir descobrir esse domínio. [Guia oficial](https://support.google.com/admob/answer/9363762?hl=en-GB).

## Referências oficiais

Consultadas em 15/10/2026:

- [Workflows GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- [Origem de publicação e planos](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
- [Domínios personalizados](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).
- [Privacidade do GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
- [Google Play: dados do usuário](https://support.google.com/googleplay/android-developer/answer/10144311?hl=pt-BR) e [URL da política](https://support.google.com/googleplay/android-developer/answer/9859455?hl=pt-BR#privacy_policy).

Confirme o comportamento dos binários finais, declarações das lojas e acesso HTTPS público antes de cadastrar a política. Testes locais não comprovam aprovação das lojas.

## Arquivos públicos e privados

Este repositório contém somente o site, suas ferramentas, testes e documentação de manutenção. O workflow publica apenas o pacote gerado a partir de `public/`.

Notas internas, capturas e dados de trabalho devem ficar em `.private/` ou `artifacts/`, ignorados pelo Git. Não adicione credenciais, certificados privados, arquivos de conta de serviço ou pacotes dos jogos. O `.gitignore` inclui essas categorias; ele não remove arquivos que já tenham sido registrados em commits anteriores.

O nome do desenvolvedor e o e-mail de atendimento presentes no site são informações públicas de contato e identificação. Para preservar um e-mail pessoal nos próximos commits, configure o endereço `noreply` fornecido pelo GitHub nas preferências de e-mail da conta.

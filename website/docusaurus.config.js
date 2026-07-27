// @ts-check
// EyeDataHub Docusaurus site config.
// Re-generate dataset pages + sidebars with:
//   python -m hub.docs.generate_dataset_pages

const { themes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'EyeDataHub',
  tagline: 'A command-line access tool and curated catalog of 251 ophthalmology data resources',
  url: 'https://khosravipooya.com',
  baseUrl: '/EyeDataHub/',

  organizationName: 'pooyakhosravi',
  projectName: 'EyeDataHub',

  onBrokenLinks: 'warn',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/pooyakhosravi/EyeDataHub/edit/main/website/',
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/eyedatahub-github-banner.png',
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      navbar: {
        title: 'EyeDataHub',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'datasetsSidebar',
            position: 'left',
            label: 'Datasets',
          },
          {
            to: '/guides/agentic',
            label: 'Agent workflows',
            position: 'left',
          },
          {
            href: 'https://github.com/pooyakhosravi/EyeDataHub',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              { label: 'Intro', to: '/' },
              { label: 'All datasets', to: '/datasets' },
            ],
          },
          {
            title: 'Community',
            items: [
              { label: 'GitHub Issues', href: 'https://github.com/pooyakhosravi/EyeDataHub/issues' },
              { label: 'CONTRIBUTING.md', href: 'https://github.com/pooyakhosravi/EyeDataHub/blob/main/CONTRIBUTING.md' },
            ],
          },
          {
            title: 'Release',
            items: [
              { label: 'EyeDataHub release DOI', href: 'https://doi.org/10.5281/zenodo.21614657' },
            ],
          },
        ],
        copyright: `Copyright ${new Date().getFullYear()} EyeDataHub. MIT licensed software; dataset terms vary.`,
      },
      prism: {
        theme: themes.github,
        darkTheme: themes.dracula,
        additionalLanguages: ['bash', 'python', 'yaml'],
      },
      colorMode: {
        defaultMode: 'light',
        respectPrefersColorScheme: true,
      },
    }),
};

module.exports = config;

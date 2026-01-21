import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'FMHY Resources',
  tagline: 'FMHY',
  favicon: 'img/fmhy pause icon.ico',

  // Set the production url of your site here
  url: 'https://fmhy-resources.pages.dev',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: 'notes',

  // GitHub pages deployment config.
  organizationName: 'fmhy', // Usually your GitHub org/user name.
  projectName: 'resources', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'notes',
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          breadcrumbs: false,
          editUrl: 'https://github.com/fmhy/resources',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  themeConfig: {
    // Replace with your project's social card
    image: 'img/fmhy pause icon.png',
    navbar: {
      title: 'FMHY Resources',
      logo: {
        alt: 'Site Logo',
        src: 'img/fmhy pause icon.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'Sidebar',
          position: 'left',
          label: 'Notes',
        },
        {
          href: 'https://github.com/fmhy/resources',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      copyright: `Copyright © ${new Date().getFullYear()} - FMHY Resources`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,

  plugins: ['docusaurus-lunr-search'],
};

export default config;

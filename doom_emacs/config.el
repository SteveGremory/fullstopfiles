;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; The creds for anything that uses them
(setq user-full-name "Steve Gremory"
      user-mail-address "stevegremory2006@gmail.com")
;; Set the theme
(setq doom-theme 'doom-laserwave)
;; Set font
(setq doom-font (font-spec :family "JetBrains Mono" :size 14))
;; Set the directory to save org files
(setq org-directory "~/org/")
;; Display line numbers?
(setq display-line-numbers-type t)
;; Enable usable scrolling
(good-scroll-mode 1)
;; Enable bidirectional sync lsp-treemacs
(lsp-treemacs-sync-mode 1)
;; Make the format on save use clang-format with the specified specs
(after! format
 (set-formatter! 'clang-format
   '("clang-format"
     "-style={BasedOnStyle: WebKit, ContinuationIndentWidth: '8', IndentWidth: '8', UseTab: Never}"
   )))

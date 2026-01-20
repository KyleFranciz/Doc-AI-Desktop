# AGENTS.md

## Scope
- Applies to the entire repository unless overridden by a deeper AGENTS.md.
- No Cursor rules found in `.cursor/rules/` or `.cursorrules`.
- No Copilot rules found in `.github/copilot-instructions.md`.

## Repository layout
- `frontend/`: Electron + React + Vite app (TypeScript).
- `frontend/electron/`: Electron main/preload code.
- `backend/firstvenv/`: Python virtualenv only (no backend source).
- `frontend/node_modules/`, `frontend/dist-electron/`: build artifacts, do not edit.

## Tooling overview
- Package manager: `npm` (see `frontend/package-lock.json`).
- Bundler: Vite with Electron plugin.
- Type checking: `tsc` (strict mode).
- Linting: ESLint with TypeScript + React Hooks rules.
- Testing: no test runner configured yet.

## Build / lint / dev commands
Run from `frontend/` unless noted.

### Install
- `npm install`

### Development
- `npm run dev`

### Build (includes typecheck + electron build)
- `npm run build`

### Preview
- `npm run preview`

### Lint (entire frontend)
- `npm run lint`

### Lint a single file
- `npm run lint -- src/routes/index.tsx`
- `npx eslint src/routes/index.tsx`

### Typecheck only
- `npx tsc --noEmit`

## Tests
- No test runner is configured in `frontend/package.json`.
- There is no documented single-test command yet.
- If tests are added later, document:
  - How to run all tests.
  - How to run a single test file.
  - How to run a single test case by name.

## Code style guidelines
Follow existing patterns in the file you touch. When in doubt, prefer clarity and consistency.

### Formatting
- No Prettier configuration detected; keep formatting consistent with nearby code.
- Use 2 spaces for indentation in JSON/TS config files.
- Use trailing commas where the surrounding code uses them.
- Keep lines reasonably short; wrap JSX props when it improves readability.

### Imports
- Order imports by group: node/electron built-ins, third-party, then local.
- Keep blank lines between import groups.
- Use named imports where possible; avoid unused imports (ESLint will flag).
- Use relative paths for local modules (no alias configured).

### TypeScript
- `strict` mode is enabled; avoid implicit `any`.
- Prefer explicit types for exported functions and component props.
- Use `type` for object shapes and `interface` for public component props when it improves readability.
- Avoid non-null assertions (`!`) unless you can justify safety.
- Favor `const` over `let`; avoid `var`.

### React
- Use function components and hooks.
- Name components in `PascalCase`.
- Keep JSX clean; extract complex UI into smaller components.
- Prefer `React.Fragment` or `<>...</>` when a wrapper is needed.
- Keep router route components small and focused.

### Electron
- `frontend/electron/main.ts` and `frontend/electron/preload.ts` should stay minimal.
- Use `contextBridge`/`ipcRenderer` patterns consistently for renderer communication.
- Avoid enabling `nodeIntegration` unless required; follow existing config.

### Naming conventions
- `camelCase` for variables, functions, hooks, and file-local helpers.
- `PascalCase` for components, types, and classes.
- Use descriptive names (avoid single-letter identifiers).

### Error handling
- Handle async errors with `try/catch` at boundaries (IPC handlers, API calls).
- Prefer returning or throwing explicit errors rather than silent failures.
- Log errors in Electron main process if they affect app startup.
- In UI code, surface user-facing errors where appropriate.

### CSS / styling
- Tailwind is configured; prefer utility classes over custom CSS when possible.
- If adding custom styles, keep them colocated and minimal.

## Files to avoid touching
- `frontend/node_modules/`
- `frontend/dist-electron/`
- `backend/firstvenv/` (virtualenv, do not edit)

## Suggested workflow for agents
1. Read relevant files to match local style.
2. Make focused edits using `edit` tool.
3. Run `npm run lint` (or lint the changed file).
4. If changes affect build, run `npm run build`.
5. Update this AGENTS.md if new tools/scripts are introduced.

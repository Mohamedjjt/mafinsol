// App.jsx — top-level state (Finance/Care identity + dark mode) and composition.
const { useState: useStateA, useEffect: useEffectA } = React;

function App() {
  const [mode, setMode] = useStateA('finance');
  const [dark, setDark] = useStateA(false);

  useEffectA(() => {
    document.body.classList.toggle('care', mode === 'care');
  }, [mode]);
  useEffectA(() => {
    document.body.classList.toggle('dark', dark);
  }, [dark]);

  const c = CONTENT[mode];

  return (
    <React.Fragment>
      <Header mode={mode} setMode={setMode} dark={dark} setDark={setDark} />
      <main>
        <Hero c={c} />
        <About c={c} />
        <Services c={c} />
        <References c={c} />
        <Workflow />
        <Contact mode={mode} />
      </main>
      <Footer c={c} />
    </React.Fragment>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);

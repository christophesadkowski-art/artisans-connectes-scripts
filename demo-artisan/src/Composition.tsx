import {
  AbsoluteFill,
  Composition,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const FPS = 30;
const DURATION = 300;

export const MyComposition = () => {
  return (
    <Composition
      id="ArtisanPresentation"
      component={ArtisanPresentation}
      durationInFrames={DURATION}
      fps={FPS}
      width={1280}
      height={720}
    />
  );
};

const BRAND = {
  bg: "#101317",
  accent: "#d9822b",
  text: "#f5f1ea",
  muted: "#9aa0a6",
};

export const ArtisanPresentation: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: BRAND.bg }}>
      <Sequence from={0} durationInFrames={100}>
        <IntroScene />
      </Sequence>
      <Sequence from={90} durationInFrames={130}>
        <ServicesScene />
      </Sequence>
      <Sequence from={210} durationInFrames={90}>
        <OutroScene />
      </Sequence>
    </AbsoluteFill>
  );
};

const Logo: React.FC<{ scale?: number }> = ({ scale = 1 }) => (
  <svg width={90 * scale} height={90 * scale} viewBox="0 0 100 100">
    <rect
      x="10"
      y="10"
      width="80"
      height="80"
      fill="none"
      stroke={BRAND.accent}
      strokeWidth="6"
    />
    <line x1="10" y1="50" x2="90" y2="50" stroke={BRAND.accent} strokeWidth="6" />
    <line x1="50" y1="10" x2="50" y2="90" stroke={BRAND.accent} strokeWidth="6" />
  </svg>
);

const IntroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoScale = spring({ frame, fps, config: { damping: 12 } });
  const titleOpacity = interpolate(frame, [10, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const titleY = interpolate(frame, [10, 30], [20, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const taglineOpacity = interpolate(frame, [30, 50], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fadeOut = interpolate(frame, [80, 100], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        opacity: fadeOut,
      }}
    >
      <div style={{ transform: `scale(${logoScale})`, marginBottom: 24 }}>
        <Logo scale={1.4} />
      </div>
      <div
        style={{
          fontFamily: "Arial, sans-serif",
          fontSize: 64,
          fontWeight: 800,
          letterSpacing: 4,
          color: BRAND.text,
          opacity: titleOpacity,
          transform: `translateY(${titleY}px)`,
        }}
      >
        ATELIER SADKOWSKI
      </div>
      <div
        style={{
          fontFamily: "Arial, sans-serif",
          fontSize: 28,
          color: BRAND.accent,
          marginTop: 16,
          opacity: taglineOpacity,
        }}
      >
        Métallerie &amp; Ferronnerie d&apos;art
      </div>
    </AbsoluteFill>
  );
};

const SERVICES = [
  "Garde-corps sur mesure",
  "Portails & clôtures",
  "Escaliers métalliques",
  "Verrières d'intérieur",
];

const ServicesScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const fadeOut = interpolate(frame, [110, 130], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        justifyContent: "center",
        paddingLeft: 140,
        opacity: fadeOut,
      }}
    >
      <div
        style={{
          fontFamily: "Arial, sans-serif",
          fontSize: 34,
          color: BRAND.muted,
          marginBottom: 30,
        }}
      >
        Nos savoir-faire
      </div>
      {SERVICES.map((service, i) => {
        const start = i * 12;
        const enter = spring({
          frame: frame - start,
          fps,
          config: { damping: 14 },
        });
        const opacity = interpolate(frame - start, [0, 10], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <div
            key={service}
            style={{
              display: "flex",
              alignItems: "center",
              opacity,
              transform: `translateX(${(1 - enter) * -60}px)`,
              marginBottom: 20,
            }}
          >
            <div
              style={{
                width: 14,
                height: 14,
                backgroundColor: BRAND.accent,
                marginRight: 20,
              }}
            />
            <div
              style={{
                fontFamily: "Arial, sans-serif",
                fontSize: 44,
                fontWeight: 700,
                color: BRAND.text,
              }}
            >
              {service}
            </div>
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

const OutroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({ frame, fps, config: { damping: 11 } });
  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        alignItems: "center",
        justifyContent: "center",
        opacity,
      }}
    >
      <div style={{ transform: `scale(${scale})`, marginBottom: 16 }}>
        <Logo scale={1} />
      </div>
      <div
        style={{
          fontFamily: "Arial, sans-serif",
          fontSize: 40,
          fontWeight: 800,
          color: BRAND.text,
        }}
      >
        Devis gratuit
      </div>
      <div
        style={{
          fontFamily: "Arial, sans-serif",
          fontSize: 26,
          color: BRAND.accent,
          marginTop: 12,
        }}
      >
        03 29 00 00 00 — atelier-sadkowski.fr
      </div>
    </AbsoluteFill>
  );
};

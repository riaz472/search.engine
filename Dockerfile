FROM searxng/searxng:latest
EXPOSE 7860
CMD ["/usr/local/searxng/docker-entrypoint.sh"]
